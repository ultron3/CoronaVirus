import mysql.connector
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="telemedicina2123",
  database="datavirus"  # Specifica il database da utilizzare
)

mycursor = mydb.cursor()

while True:
    print("Menu:")
    print("1. Select")
    print("2. Insert")
    print("3. Delete")
    print("4.Plot")
    print("5. Linear Regression")
    print("6. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        mycursor.execute("SELECT * FROM virus")
        myresult = mycursor.fetchall()
        if not myresult:
            print("No data available.")
        else:
            table = PrettyTable()
            table.field_names = ["ID", "State", "Positive", "Negative", "Total"]
            for row in myresult:
                table.add_row(row)

            print(table)
    
    elif choice == "2":
        state = input("Enter the state: ")
        positive = int(input("Enter the number of positive: "))
        negative = int(input("Enter the number of negative: "))
        tot = positive + negative

        sql = "INSERT INTO virus (state, positive, negative, tot) VALUES (%s, %s, %s, %s);"
        val = (state, positive, negative, tot)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    
    elif choice == "3":
        state_to_delete = input("Enter the state to delete: ")
        delete_sql = "DELETE FROM virus WHERE state = %s"
        delete_val = (state_to_delete,)
        mycursor.execute(delete_sql, delete_val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted.")
    
    elif choice == "4":
        mycursor.execute("SELECT state, positive,negative FROM virus")
        myresult = mycursor.fetchall()

        states = [row[0] for row in myresult]
        positives = [row[1] for row in myresult]
        negatives = [row[2] for row in myresult]

        plt.figure(figsize=(10, 6))
        plt.bar(states, positives, label='Positive', alpha=0.7, color='b')
        plt.bar(states, negatives, label='Negative', alpha=0.7, color='r', bottom=positives)
        plt.xlabel('State')
        plt.ylabel('Total')
        plt.title('Total Cases by State')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()
    
    elif choice=="5":
        mycursor.execute("SELECT state, positive,negative FROM virus")
        myresult = mycursor.fetchall()
        positives = [row[1] for row in myresult]
        negatives = [row[2] for row in myresult]

        x = np.array(positives)
        y = np.array(negatives)

        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

        plt.scatter(x, y, label='Dati')
        plt.plot(x, slope * x + intercept, color='r', label='Regressione Lineare')
        plt.xlabel('Positives')
        plt.ylabel('Negatives')
        plt.title('Regressione Lineare tra Positives e Negatives')
        plt.legend()
        plt.show()

    elif choice == "6":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
