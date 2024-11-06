from flask import Flask, request, redirect, url_for, render_template
import json
import os

app = Flask(__name__)
json_file_path = 'data.json'
def create_json_file():
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as json_file:
            json.dump([], json_file)
def save_to_json(data):
    create_json_file()
    with open(json_file_path, 'r+') as json_file:
        file_data = json.load(json_file)
        file_data.append(data)
        json_file.seek(0)
        json.dump(file_data, json_file, indent=4)


@app.route('/main')
def index():
    return render_template('main.html')

@app.route('/admin')
def reservations():
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            reservations_data = json.load(json_file)
    else:
        reservations_data = []

    return render_template('admin.html', reservations=reservations_data)



@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    people = request.form['people']
    date = request.form['date']
    clock = request.form['clock']

    data = {
        'name': name,
        'email': email,
        'number': number,
        'people': people,
        'date': date,
        'clock': clock
    }

    save_to_json(data)
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)