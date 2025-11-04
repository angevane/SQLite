from collections.abc import ValuesView
from pickle import INT
import sqlite3


executar = sqlite3.connect("Livros.db")

cursor = executar.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS Livros (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               titulo TEXT NOT NULL UNIQUE, 
               autor TEXT, 
               ano INTEGER,
               genero TEXT, 
               disponivel INTEGER)
                """)

import sqlite3
con = sqlite3.connect("Livros.db")
cur = con.cursor()

livros = [
    ('A Sombra do Vento', 'Carlos Ruiz', 'Zafón', 2001, 'Mistério', 1),
    ('1984', 'George Orwell',1949, 'Ficção Científica', 0),
    ('O Senhor dos Anéis', 'J.R.R. Tolkien',1954, 'Fantasia', 1),
    ('Dom Quixote', 'Miguel de Cervantes',1605, 'Romance', 1),
    ('Cem Anos de Solidão', 'Gabriel García Márquez',1967, 'Realismo Mágico', 0)
]