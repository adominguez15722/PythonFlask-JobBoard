from email.policy import default
from multiprocessing import connection
from flask import Flask, render_template, g
import sqlite3
PATH = 'db/jobs.sqlite'


app = Flask(__name__)


def open_connection():
    getattr(g, '_connection')
    if connection is None:
        connection = g._connection = sqlite3.connect(PATH)
    return getattr(connection)


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)