from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global task_id_counter
    task_desc = request.form.get('task')
    if task_desc:
        tasks.append({"id": task_id_counter, "task": task_desc, "completed": False})
        task_id_counter += 1
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
# Simple To-Do List Application using Flask