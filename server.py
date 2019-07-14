from flask import Flask, render_templates, redirect, session, flash, request
from mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'donttellanyone'


@app.route('/')
def main():
    return render_templates('index.html')


if __name__ == "__main__":
    app.run(debug=True)
