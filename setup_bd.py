# Créer une base de données, avec le bon schéma

# Article(id, title, slug, content, author, date)
# Comment(comment_id, title, content, article_id)

import sqlite3

connexion = sqlite3.connect('api_data.db')

cursor = connexion.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""CREATE TABLE IF NOT EXISTS article (
                  article_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title VARCHAR(256),
                  slug VARCHAR(256),
                  content TEXT,
                  author VARCHAR(64),
                  date DATETIME
               )""")

cursor.execute("""
                CREATE TABLE IF NOT EXISTS comment(
                comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(256),
                content TEXT,
                article_id INTEGER,
                FOREIGN KEY (article_id)
                REFERENCES article (id));
            """)

connexion.commit()

connexion.close()