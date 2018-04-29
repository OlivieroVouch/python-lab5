from flask import Flask # import flask package
from flask import render_template,url_for, request, redirect  # function from Flask package

app = Flask(__name__)
import todo_database

@app.route('/index')
def index():
    list = todo_database.showTask()
    return render_template("index.html", result=list)

@app.route('/')
def hello_world():
    return redirect(url_for('index'))  # return the content of the page--> actually here we are not yet returning an HTML file but just a stringreturn redirect(url_for('index')) # return the content of the page--> actually here we are not yet returning an HTML file but just a string

@app.route('/delete/<id_task>')
def delete(id_task):
    todo_database.db_check_remove(id_task)
    return render_template("delete.html")

@app.route('/new_task', methods=['POST'])
def new_task():
    task = request.form['task']
    todo_database.new_Task(task)
    return render_template("new_task.html",task=task)


if __name__ == '__main__':
    app.run()
