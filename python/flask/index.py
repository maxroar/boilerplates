from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

@app.route('/')
def display_index():
    return render_template('index.html')

app.run(debug=True)
