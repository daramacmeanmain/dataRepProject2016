#Adapted from https://github.com/data-representation/example-sqlite

import sqlite3

DATABASE = 'data/project.db'

conn = sqlite3.connect(DATABASE)
c = conn.cursor()

#Create tables
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS messageTable(messageId INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS userTable(userId INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT)')

if __name__ == "__main__":
    create_table()