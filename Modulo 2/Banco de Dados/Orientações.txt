import sqlite3

empresa =  sqlite3.connect('empresa.db')

cursor = empresa.cursor()


cursor.execute("INSERT INTO funcionarios VALUES( 6,'Lucas','Estagiario',6.0000,'RH')")
empresa.commit()


cursor.execute("SELECT * FROM funcionarios")

import sqlite3

escola =  sqlite3.connect('escola.db')

cursor = escola.cursor()


escola.commit()

cursor.execute("SELECT* FROM alunos")
print(cursor.fetchall())


import sqlite3

loja =  sqlite3.connect('loja.db')

cursor = loja.cursor()


cursor.execute("SELECT* FROM vendas")
print(cursor.fetchall())


import sqlite3

cinema =  sqlite3.connect('cinema.db')

cursor = cinema.cursor()

cursor.execute("SELECT* FROM filmes")
print(cursor.fetchall())
