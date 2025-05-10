from flask import Flask, request, jsonify, render_template, redirect, url_for
app = Flask(__name__)

tasks = []
task_id_counter = 1

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def add_task():
    global task_id_counter
    title = request.form.get('title') or request.json.get('title')
    new_task = {'id': task_id_counter, 'title': title, 'done': False}
    tasks.append(new_task)
    task_id_counter += 1

    if request.form:
        return redirect(url_for('home'))
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['POST', 'DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]

    if request.form.get('from_form'):
        return redirect(url_for('home'))

    return jsonify({'message': 'Task deleted'}), 200


@app.route('/health')
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
