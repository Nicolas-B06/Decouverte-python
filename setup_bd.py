# Article: title, slug, content, author, date
# Coment: coment_id, content, article_id
import sqlite3

connexion = sqlite3.connect('Sqllite_database')
cursor=connexion.cursor()

cursor.execute( """CREATE TABLE article(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	title  VARCHAR (255),
   	slug  VARCHAR (255),
	content TEXT,
    author  VARCHAR (255),
    date DATETIME 
	)""") 

cursor.execute( """CREATE TABLE comment(
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
	content TEXT,
    article_id INTEGER,
    FOREIGN KEY (article_id) REFERENCES article(id)
	)""") 

connexion.commit()

connexion.close()