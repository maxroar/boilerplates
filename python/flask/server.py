from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'key' #change this

mysql = MySQLConnector(app, 'db')
#all routes go here
@app.route('/')
def display_index():
    return render_template('index.html')
# an example of running a query
print mysql.query_db("SELECT * FROM table")
app.run(debug=True)
