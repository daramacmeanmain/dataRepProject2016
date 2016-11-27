import flask as fl
import sqlite3

DATABASE = 'data/project.db'

app = fl.Flask(__name__)

@app.route("/")
def root():
    return app.send_static_file('index.html')

def get_db():
    db = getattr(fl.g, '_database', None)
    if db is None:
        db = fl.g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(fl.g, '_database', None)
    if db is not None:
        db.close()

@app.route('/data', methods=["GET", "POST"])
def user_data():
    conn = sqlite3.connect(DATABASE)
    c = get_db().cursor()
    c.execute("SELECT * FROM userTable")
    return str(c.fetchall())

if __name__ == "__main__":
    app.run()