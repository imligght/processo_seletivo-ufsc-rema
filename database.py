import sqlite3

connection = sqlite3.connect("data.db")


cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS data_table (
               id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,
               age INTEGER
               )''')

def insert_data(dados):
    cursor.execute("INSERT INTO data_table (dados) VALUES (?)" (dados))
    connection.commit()
    print("Data inserted sucessfully.")

def retrieve_data():
    cursor.execute("SELECT * FROM data_table")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Dado: {row[1]}")


retrieve_data()

cursor.close()
connection.close()