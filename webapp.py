import flask as fl 
from flask import render_template, request, g
import sqlite3

DATABASE = 'data/project.db'
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

app = fl.Flask(__name__)

@app.route("/")
def root():
    return app.send_static_file('index.html')

def get_db():
    db = getattr(fl.g, '_database', None)
    if db is None:
        db = fl.g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/data', methods = ['GET', 'POST'])        
def update_db():
    c.execute("INSERT INTO messageTable(message) VALUES(?)",(fl.request.form['messageInput'],))
    conn.commit()
    return str(c.fetchall())

@app.route('/dataBase', methods=["GET", "POST"])
def user_data():
    conn = sqlite3.connect(DATABASE)
    c = get_db().cursor()
    c.execute("SELECT * FROM messageTable")
    return str(c.fetchall())



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(fl.g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run()