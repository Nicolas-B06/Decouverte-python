
from fastapi import FastAPI
import sqlite3

app = FastAPI()
connexion = sqlite3.connect("Sqllite_database")
cursor = connexion.cursor()



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/articles")
async def  fetchall():
    result= cursor.execute( """SELECT * FROM article""")
    return result

connexion.close()