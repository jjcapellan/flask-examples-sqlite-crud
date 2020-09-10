from flask import Blueprint, make_response
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