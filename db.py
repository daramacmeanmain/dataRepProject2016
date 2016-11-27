import sqlite3

DATABASE = 'data/project.db'

conn = sqlite3.connect(DATABASE)
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS userTable(id INTEGER, name TEXT)')
    
def data_entry():
    id = 123
    name = 'Test'
    c.execute("INSERT INTO userTable (id, name) VALUES(?, ?)", (id, name))
    conn.commit()
    

if __name__ == "__main__":
    create_table()
    data_entry()