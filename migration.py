import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="telemedicina2123",
  database="datavirus"  # Specifica il database da utilizzare
)

mycursor = mydb.cursor()


import psycopg2

# Connessione al database PostgreSQL
conn_postgresql = psycopg2.connect(
    database="nome_database_postgresql",
    user="nome_utente_postgresql",
    password="utente",
    host="localhost",
    port="5432"  # Porta predefinita di PostgreSQL
)


cursor_mysql = conn_mysql.cursor()

cursor_mysql.execute("SELECT * FROM SELECT * FROM virus")

dati_mysql = cursor_mysql.fetchall()


cursor_postgresql = conn_postgresql.cursor()

for riga in dati_mysql:
    cursor_postgresql.execute(
        "INSERT INTO  virus(column1, column2, column3,column4,column5) VALUES (%s, %s,%s,%s,%s)",
        riga
    )

# Fai il commit delle modifiche
conn_postgresql.commit()