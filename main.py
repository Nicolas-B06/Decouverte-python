import sqlite3

from datetime import datetime
from sqlite3.dbapi2 import Cursor
from fastapi import FastAPI, HTTPException
#Serveur web
import uvicorn

from models.Article import OutArticle, InArticle
from models.Comment import OutComment, InComment

app = FastAPI(title="Mon premier blog")
# connection à la bdd
connection = sqlite3.connect('api_data.db')


@app.get("/articles")
async def get_articles():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Article')
    articles_db = cursor.fetchall()
    articles_obj = []
    for data in articles_db:
        articles_obj.append(OutArticle(
            article_id=data[0],
            title=data[1],
            slug=data[2],
            content=data[3],
            author=data[4],
            date=datetime.strptime(data[5], '%Y-%m-%d %H:%M:%S')
        )
        )
    cursor.close()
    return articles_obj


@app.get("/articles/{article_id}", response_model=OutArticle)
async def get_article(article_id: int):
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM article WHERE article_id = :toto",
        {"toto": article_id}
    )

    article_db = cursor.fetchone()
    if article_db is None:
        raise HTTPException(status_code=404, detail="L'article n'existe pas")

    article_obj = OutArticle(
        article_id=article_db[0],
        title=article_db[1],
        slug=article_db[2],
        content=article_db[3],
        author=article_db[4],
        date=datetime(2021, 1, 1, 23, 58, 0)

    )
    cursor.close()
    return article_obj



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


