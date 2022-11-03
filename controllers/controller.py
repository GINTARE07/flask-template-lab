from flask import render_template, request
from app import app
from models.todo_list import tasks
from models.task import Task
from models.todo_list import tasks, add_new_task

@app.route('/tasks')
def index():
    return render_template('index.html', title='Home', tasks=tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task_title = request.form['title']
    task_description = request.form['description']
    new_task = Task(task_title, task_description, False)
    add_new_task(new_task)
    return render_template('index.html', title='Home', tasks=tasks)

