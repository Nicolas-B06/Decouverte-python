import math
import sqlite3

from datetime import datetime
# Permet de typer certain paramètres (via interface)
from typing import Optional, List
from urllib.parse import parse_qs

# Import du framework
# + classe d'exception HTTP (qui sera catch par le framework au raise dans notre code)
# + classe qui représente la requête (injecté comme dépendance lorsque le paramètre est présent dans une méthode)
from fastapi import FastAPI, HTTPException, Request

# Serveur web (écoute sur un port et parse les requêtes HTTP)
import uvicorn
from fastapi.params import Query
from starlette.middleware.cors import CORSMiddleware

# Import de nos modèles défini dans le module/dossier "model"
from models.Article import OutArticle, InArticle
from models.Comment import OutComment, InComment
from models.HAL import Links

# Instancie un objet FastAPI, avec comme argument nommé title "Mon premier blog"
app = FastAPI(title="Mon premier blog")

# Liste des domaines à partir desquelles notre API sera autorisé à répondre
origins = [
    "http://localhost:8080",
    "http://localhost:8000",
]

# Configuration CORS (Cross Origin Resource Sharing),
# On y intègre le tableau "origins" avec nos domaines autorisés
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# connection à l BD (grâce au module sqlite3)
connection = sqlite3.connect('api_data.db')


@app.get("/articles/search")
async def search_articles(request: Request):
    # Ici on injecte notre objet Request, qui représente la requête HTTP
    # il a un attribut query_params qui contient les paramètres de requête
    # on peut caster en string afin d'avoir la chaine à partir du "?"
    params = str(request.query_params)
    cursor = connection.cursor()
    # on initialise la chaine pour les conditions de notre SELECT WHERE
    like_condition = ""
    # on récupère les paramètres parsés
    qs = parse_qs(params)
    # Les champs sur lequels on autorise la recherche
    known_fields = ['title', 'slug', 'content', 'author']
    # On parcoure les paramètre, si le champs est autorisé, on concatène la condition associée
    for k, v in qs.items():
        if k in known_fields:
            # Méthode avec concaténation simple
            # like_condition += "AND " + k + " LIKE '%" + v[0] + "%' "
            # Méthode avec fstring
            like_condition += f"AND {k} LIKE '%{v[0]}%' "
    cursor.execute('SELECT * FROM Article WHERE 1 ' + like_condition)
    articles_db = cursor.fetchall()
    cursor.close()
    articles = []
    # on instancie nos articles en fonctiond des retours de la BD
    for db_article in articles_db:
        articles.append(
            create_article_from_db(db_article).dict()
        )

    links = Links(self=request.url.path, parent="/articles").dict(include={'self', 'parent'})

    return {"_links": links, "articles": articles}

"""
Fonctionnement du paramètre "page" :
/articles => page1 par défaut
5 elements par page donc :
/articles?page=2 => 5 articles depuis le 6 au 10 
/articles?page=99 => [] (si aucun article n'existe dans la page)
"""
@app.get("/articles")
async def get_articles(page: Optional[int] = 0, f: Optional[List[str]] = Query(None)):
    # page et f sont des query string parameters
    # comme ils n'apparaissent pas dans le endpoint (pas de /articles/{page} par exemple)
    # il seront donc forcément interprété en query param (?page=1&f=title)
    cursor = connection.cursor()

    # COUNT ROW
    rows_query = "SELECT Count() FROM Article"
    cursor.execute(rows_query)
    last_page = math.ceil(cursor.fetchone()[0] / 5)

    # GET ARTICLES
    page = page or 1  # Null coalescing equivalent
    cursor.execute(
        "SELECT * FROM Article limit :limit offset :offset",
        {"limit": 5, "offset": (page - 1) * 5}
    )
    db_articles = cursor.fetchall()
    cursor.close()
    articles = []
    for db_article in db_articles:
        if f is not None:
            articles.append(create_article_from_db(db_article).dict(include=set(f)))
        else:
            articles.append(create_article_from_db(db_article))
    if page > 1:
        prev_page = f"/articles?page={page - 1}"
    else:
        prev_page = None
    if page < last_page:
        next_page = f"/articles?page={page + 1}"
    else:
        next_page = None
    links = Links(
        self=f"/articles?page={page}",
        parent="/",
        prev=prev_page,
        next=next_page,
        last=f"/articles?page={last_page}",
        search="/articles/search").dict(include={'self', 'parent', 'prev', 'next', 'last', 'search'})
    return {"_links": links, "articles": articles}


@app.get("/articles/{article_id}")
async def get_article(article_id: int):
    c = connection.cursor()
    article = await fetch_article(article_id, c)
    # LAST ID
    c.execute("SELECT MAX(article_id) FROM Article")
    last_id = c.fetchone()[0]
    c.close()
    out_article = OutArticle(
        article_id=article.article_id,
        title=article.title,
        slug=article.slug,
        content=article.content,
        author=article.author,
        date=article.date,
    ).dict()
    if article_id != 1:
        prev_art = f"/articles/{article_id - 1}"
    else:
        prev_art = None
    if article_id != last_id:
        next_art = f"/articles/{article_id + 1}"
    else:
        next_art = None
    out_article['_links'] = Links(
        self=f"/articles/{article_id}",
        parent="/articles/",
        prev=prev_art,
        next=next_art,
        search="/articles/search",
        last=f"/articles/{last_id}",
        children=[f"/articles/{article_id}/comments"],
    )
    return out_article


@app.post("/articles", status_code=201)
async def create_article(article: InArticle):
    c = connection.cursor()
    article_values = {
        "title": article.title,
        "slug": article.slug,
        "content": article.content,
        "author": article.author,
        "date": article.date
    }
    last_id = c.execute(
        "INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);",
        article_values).lastrowid
    connection.commit()
    c.close()
    article_id = last_id
    out_article = OutArticle(
        article_id=article_id,
        title=article.title,
        slug=article.slug,
        content=article.content,
        author=article.author,
        date=article.date,
    ).dict()
    if article_id != 1:
        prev_art = f"/articles/{article_id - 1}"
    else:
        prev_art = None
    if article_id != last_id:
        next_art = f"/articles/{article_id + 1}"
    else:
        next_art = None
    out_article['_links'] = Links(
        self=f"/articles/{article_id}",
        parent="/articles/",
        prev=prev_art,
        next=next_art,
        search="/articles/search",
        last=f"/articles/{last_id}",
        children=[f"/articles/{article_id}/comments"],
    )
    return out_article


@app.put("/articles/{article_id}", status_code=200)
async def put_article(article_id: int, article: InArticle):
    c = connection.cursor()
    await fetch_article(article_id, c)
    article_values = {
        "id": article_id,
        "title": article.title,
        "slug": article.slug,
        "content": article.content,
        "author": article.author,
        "date": article.date
    }
    c.execute("""UPDATE article 
                 SET title = :title,
                     slug = :slug,
                     content = :content,
                     author = :author,
                     date = :date
                 WHERE article_id = :id;""", article_values)
    connection.commit()
    article = await fetch_article(article_id, c)
    c.execute("SELECT MAX(article_id) FROM Article")
    last_id = c.fetchone()[0]
    c.close()
    out_article = OutArticle(
        article_id=article_id,
        title=article.title,
        slug=article.slug,
        content=article.content,
        author=article.author,
        date=article.date,
    ).dict()
    if article_id != 1:
        prev_art = f"/articles/{article_id - 1}"
    else:
        prev_art = None
    if article_id != last_id:
        next_art = f"/articles/{article_id + 1}"
    else:
        next_art = None
    out_article['_links'] = Links(
        self=f"/articles/{article_id}",
        parent="/articles/",
        prev=prev_art,
        next=next_art,
        search="/articles/search",
        last=f"/articles/{last_id}",
        children=[f"/articles/{article_id}/comments"],
    )
    return out_article


@app.delete("/articles/{article_id}", status_code=204)
async def delete_article(article_id: int):
    c = connection.cursor()
    await fetch_article(article_id, c)
    c.execute('DELETE FROM Article WHERE article_id=:id', {"id": article_id})
    connection.commit()
    c.close()
    return None


# ------------------------------ COMMENT ENDPOINTS ------------------------------

@app.get("/articles/{article_id}/comments", status_code=200)
async def get_comments(article_id: int):
    c = connection.cursor()
    await fetch_article(article_id, c)
    c.execute("SELECT * FROM Comment WHERE article_id = :id", {"id": article_id})
    db_comments = c.fetchall()
    comments = []
    for data in db_comments:
        comments.append(create_comment_from_db(data))
    c.close()
    links = Links(self=f"/articles/{article_id}/comments", parent=f"/articles/{article_id}").dict(
        include={'self', 'parent'})
    return {"comments": comments, "_links": links}


@app.get("/articles/{article_id}/comments/{comment_id}")
async def get_comment(article_id: int, comment_id: int):
    c = connection.cursor()
    await fetch_article(article_id, c)
    c.execute(
        "SELECT * FROM Comment WHERE article_id = :article_id AND comment_id = :comment_id",
        {"article_id": article_id, "comment_id": comment_id}
    )
    db_comment = c.fetchone()
    if db_comment is None:
        raise HTTPException(status_code=404, detail='Commentaire inconnu')
    return create_comment_from_db(db_comment)


@app.post("/articles/{article_id}/comment", status_code=201)
async def create_comment(article_id: int, comment: InComment):
    c = connection.cursor()
    await fetch_article(article_id, c)
    comment_values = {
        "title": comment.title,
        "content": comment.content,
        "article_id": article_id,
    }
    c.execute("INSERT INTO Comment(title, content, article_id) VALUES(:title, :content, :article_id);",
              comment_values)
    connection.commit()
    c.close()


# ----------------------------------- PRIVATES -----------------------------------

async def fetch_article(article_id, c):
    c.execute("SELECT * FROM Article WHERE article_id = :id", {"id": article_id})
    article = c.fetchone()
    if article is None:
        c.close()
        raise HTTPException(status_code=404, detail='Article inconnu')
    else:
        return create_article_from_db(article)


def create_article_from_db(d: list):
    if type(d[5]) is str:
        date = d[5]
    else:
        date = datetime.strptime(d[5], '%Y-%m-%d %H:%M:%S')

    return OutArticle(
        article_id=d[0],
        title=d[1],
        slug=d[2],
        content=d[3],
        author=d[4],
        date=date
    )


def create_comment_from_db(d: list):
    return OutComment(id=d[0], title=d[1], content=d[2])


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
