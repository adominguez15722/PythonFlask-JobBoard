from flask import Flask, render_template, g
import sqlite3
PATH = 'db/jobs.sqlite'


app = Flask(__name__)


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)