from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Load lecture data from subject-specific JSON files
def load_lectures():
    subjects = ['tinyml', 'iot', 'ai', 'mechanics', 'robotics']
    all_lectures = {"lectures": []}
    for subject in subjects:
        file_path = f'{subject}.json'
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                all_lectures['lectures'].extend(data['lectures'])
        except FileNotFoundError:
            print(f"Warning: {file_path} not found")
            continue
    return all_lectures

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/lectures')
def get_lectures():
    return jsonify(load_lectures())

if __name__ == '__main__':
    app.run(debug=True)