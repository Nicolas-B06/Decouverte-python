import sqlite3

from datetime import datetime
from fastapi import FastAPI, HTTPException
import uvicorn

from models.Article import OutArticle, InArticle

app = FastAPI(title="Mon premier blog")

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

@app.post("/articles")
async def create_article(article: InArticle):
    article_dict=article.dict
    return article_dict

@app.put("/articles/{article_id}")
async def create_article(article_id: int, article: InArticle):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM article WHERE article_id = :toto",
        {"toto": article_id}
    )
    article_db = cursor.fetchone()
    if article_db is None:
        raise HTTPException(status_code=404, detail="L'article n'existe pas")
    
    cursor.close()
    return {"article_id": article_id, **article.dict()}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

