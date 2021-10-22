import sqlite3
import math

from datetime import datetime
# Permet de typer certain paramètres (via interface)
from typing import Optional, List

# Import du framework
# + classe d'exception HTTP (qui sera catch par le framework au raise dans notre code)
from urllib.parse import parse_qs

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.params import Query

# Serveur web (écoute sur un port et parse les requêtes HTTP)
import uvicorn

# Import de nos modèles défini dans le module/dossier "model"
from models.Article import OutArticle, InArticle
from models.Comment import OutComment, InComment
from models.HAL import Links

# Instancie un objet FastAPI, avec comme argument nommé title "Mon premier blog"
app = FastAPI(title="Mon premier blog")

# connection à l BD (grâce au module sqlite3)
connection = sqlite3.connect('api_data.db')


# /articles => page1
# 5 elements par page
# /articles?page=3
# /articles?page=99 => []
"""
Récupère tous les articles, paginés par 5
On utilise un décorateur pour étendre les fonctions de notre objet "app" (soit le FastApi)
les paramètres fournis (page, f) sont interprété comme des param de requêtes (Query Parameters)
"""
@app.get("/articles")
async def get_articles(page: int = 1, f: List[str] = Query(None)):
    # On crée un pointeur en BD (un cursor)
    cursor = connection.cursor()
    # on récupère nos articles en limitant les résultats
    cursor.execute(f"SELECT * FROM Article LIMIT 5 OFFSET {5 * (page -1)}")
    # on récupère tout dans db_articles
    db_articles = cursor.fetchall()
    # on ferme la connexion (OBLIGATOIRE)
    
    articles = []
    # rempli le tableau avec des articles castés en dictionnaires
    # l'argument nommé include autorise une liste blanche des champs de l'article
    for db_article in db_articles:
        # Si des champs sont précisés, on les include, sinon on caste en dict simplement
        if f is not None:
            articles.append(
                create_article_from_db(db_article).dict(include=set(f))
            )
        else:
            articles.append(
                create_article_from_db(db_article).dict()
            )
            
    max_article= cursor.execute( "SELECT COUNT(*) FROM article ")
    cursor.close()
    max_page = math.ceil(max_article // 5 )
    
    prev = None
    if page != 1:
        prev = f"articles?page={page-1}"
    
    next = None
    if page != max_page:
        next = f"articles?page={page+1}"
        
    links =  Links(
        self=  f"articles?page={page}",
        next= next,
        prev= prev,
        parent= "/",
        last= f"articles?page={max_page}",
        first= "/articles?page=1",
        search= "/articles/search"
    )  
   
    return {"articles": articles, "links": links }

"""
/search?title=santé&author=AFP
"""
@app.get("/articles/search")
async def search_article(request: Request):
    # On récupère une librairie de parse de Query String : urllib
    # qui expose la méthode parse_qs pour parser les query string parameters
    params = str(request.query_params)
    # conteneur_iterable = [ element pushé for element in elements if condition ]
    """
    exemple compréhension de liste
    nombres = [1,2,3,4,5]
    nombres_filtered_doubled = [nombre for nombre in nombres]
    nombres_filtered_doubled = [nombre *2 for nombre in nombres]
    nombres_filtered_doubled = [nombre *2 for nombre in nombres if nombre > 2]
    """
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
            # like_condition += "AND " + k + " LIKE '%" + v[0] + "%' "
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
    return articles


@app.get("/articles/{article_id}")
async def get_article(article_id: int, response: Response):
    c = connection.cursor()
    article = await fetch_article(article_id, c)
    c.close()
    #Cache-Control: max-age
    response.headers["Cache-Control"] = "max-age=3600"
    return article


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
    lastrowid = c.execute(
        "INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);",
        article_values).lastrowid
    connection.commit()
    article = await fetch_article(lastrowid, c)
    c.close()
    return article


@app.put("/articles/{article_id}", response_model=OutArticle, status_code=200)
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
    c.close()
    return article


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
    return comments


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