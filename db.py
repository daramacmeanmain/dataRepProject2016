import sqlite3

DATABASE = 'data/project.db'

conn = sqlite3.connect(DATABASE)
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS messageTable(id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)')
    


if __name__ == "__main__":
    create_table()
    ##data_entry()