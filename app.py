from flask import Flask # import flask package
from flask import render_template,url_for, request, redirect, session# function from Flask package

app = Flask(__name__)
import todo_database

@app.route('/index')
def index():
    list = todo_database.showTask()
    return render_template("index.html", result=list)

@app.route('/')
def hello_world():
    return redirect(url_for('index'))  # return the content of the page--> actually here we are not yet returning an HTML file but just a stringreturn redirect(url_for('index')) # return the content of the page--> actually here we are not yet returning an HTML file but just a string


if __name__ == '__main__':
    app.run()
