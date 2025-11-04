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

INSERT INTO Livros (titulo, autor, ano, genero, disponivel) VALUES
('A Sombra do Vento', 'Carlos Ruiz', 'Zafón', 2001, 'Mistério', 1),
('1984', 'George Orwell',1949, 'Ficção Científica', 0)
('O Senhor dos Anéis', 'J.R.R. Tolkien',1954, 'Fantasia', 1)
('Dom Quixote', 'Miguel de Cervantes',1605, 'Romance', 1)
('Cem Anos de Solidão', 'Gabriel García Márquez',1967, 'Realismo Mágico', 0);
