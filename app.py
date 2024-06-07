from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Company's Employee Salary API!"

@app.route('/employees')
def get_employees():
    with open('employees.json') as f:
        employees = json.load(f)
    return jsonify(employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

