from flask import Blueprint, make_response, request
from app.db import get_db
import json

bp = Blueprint('crud', __name__)

@bp.route('/employees', methods=['GET'])
def employees():
    db = get_db()
    employees_list = db.execute('SELECT * FROM employees;').fetchall()

    return make_response(json.dumps([dict(row) for row in employees_list]), 200)


@bp.route('/employee/<string:name>')
def employee(name):
    db = get_db()
    employee_row = db.execute('SELECT * FROM employees WHERE name = ?;', (name,)).fetchone()

    return make_response(json.dumps(dict(employee_row)), 200)


@bp.route('/department/<string:department>')
def department(department):
    db = get_db()
    employees_by_department_list = db.execute('SELECT * FROM employees WHERE department = ?', (department,)).fetchall()

    return make_response(json.dumps([dict(row) for row in employees_by_department_list]), 200)


@bp.route('/add', methods=['POST'])
def add():
    db = get_db()
    data = request.get_json()
    try:
        db.execute('INSERT INTO employees (name, department, age, salary) VALUES (?,?,?,?);',\
             (data['name'], data['department'], data['age'], data['salary'],))
        db.commit()
    except:
        return make_response('Invalid data', 400)

    return make_response('New employee registered', 200)