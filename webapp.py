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

@app.route('/userData', methods = ['GET', 'POST'])
def update_userData():
    c.execute("INSERT INTO userTable(user) VALUES(?)",(fl.request.form['userInput'],))
    conn.commit()
    return str(c.fetchall())

@app.route('/messageData', methods = ['GET', 'POST'])        
def update_messageData():
    c.execute("INSERT INTO messageTable(message) VALUES(?)",(fl.request.form['messageInput'],))
    conn.commit()
    return str(c.fetchall())

##@app.route('/userDataBase', methods=["GET", "POST"])
##def user_data():
##    conn = sqlite3.connect(DATABASE)
##    c = get_db().cursor()
    ##for row in c.execute("SELECT message FROM messageTable ORDER BY id DESC"):
    ##message = row[0]
##    c.execute("SELECT user FROM userTable ORDER BY userId DESC")
##    return str(c.fetchall())

##@app.route('/messageDataBase', methods=["GET", "POST"])
##def message_data():
##    conn = sqlite3.connect(DATABASE)
##    c = get_db().cursor()
 ##   c.execute("SELECT message FROM messageTable ORDER BY messageId DESC")
##    return str(c.fetchall())

@app.route('/dataBase', methods=["GET", "POST"])
def user_data():
    conn = sqlite3.connect(DATABASE)
    c = get_db().cursor()
    ##for row in c.execute("SELECT message FROM messageTable ORDER BY id DESC"):
    ##message = row[0]
    dataOutput = c.execute("SELECT user, message FROM messageTable INNER JOIN userTable on userTable.userId = messageTable.messageId ORDER BY messageId DESC").fetchall()
    return render_template('index.html', dataOutput=dataOutput)
    
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(fl.g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run()