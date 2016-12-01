#Adapted from https://github.com/data-representation/example-sqlite

import flask as fl 
from flask import render_template, request, g
import sqlite3

DATABASE = 'data/project.db'
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

app = fl.Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

def get_db():
    db = getattr(fl.g, '_database', None)
    if db is None:
        db = fl.g._database = sqlite3.connect(DATABASE)
    return db

#Insert data from Name Input
@app.route('/userData', methods = ['GET', 'POST'])        
def update_userData():
    c.execute("INSERT INTO userTable(user) VALUES(?)",(fl.request.form['userInput'],))
    conn.commit()
    return str(c.fetchall())

#Insert data from Message Input
@app.route('/messageData', methods = ['GET', 'POST'])
def update_messageData():
    c.execute("INSERT INTO messageTable(message) VALUES(?)",(fl.request.form['messageInput'],))
    conn.commit()
    return str(c.fetchall())

#Output data from the database to index.html
@app.route('/dataBase', methods=["GET", "POST"])
def user_data():
    conn = sqlite3.connect(DATABASE)
    c = get_db().cursor()
    dataOutput = c.execute("SELECT DISTINCT user, message FROM messageTable INNER JOIN userTable on userTable.userId = messageTable.messageId ORDER BY messageId DESC").fetchall()
    return render_template('index.html', dataOutput=dataOutput)

#Close database
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(fl.g, '_database', None)
    if db is not None:
        db.close()

#run app
if __name__ == "__main__":
    app.run()