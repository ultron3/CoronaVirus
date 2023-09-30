import mysql.connector
import psycopg2
import mysql as conn_mysql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="telemedicina2123",
  database="datavirus"  # Specifica il database da utilizzare
)



# Connessione al database PostgreSQL
conn_postgresql = psycopg2.connect(
    database="datavirus",
    user="root",
    password="utente",
    host="localhost",
    port="5432"  # Porta predefinita di PostgreSQL
)


cursor_mysql = conn_mysql.cursor()

cursor_mysql.execute("SELECT *  FROM datavirus.virus")

dati_mysql = cursor_mysql.fetchall()


cursor_postgresql = conn_postgresql.cursor()

for riga in dati_mysql:
    cursor_postgresql.execute(
        "INSERT INTO  virus(column1, column2, column3,column4,column5) VALUES (%s, %s,%s,%s,%s)",
        riga
    )

# Fai il commit delle modifiche
conn_postgresql.commit()

cursor_mysql.close()
conn_mysql.close()

cursor_postgresql.close()
conn_postgresql.close()
