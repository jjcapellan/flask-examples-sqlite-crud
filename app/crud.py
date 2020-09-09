from flask import Blueprint, request, make_response, jsonify
from app.db import get_db
import json

bp = Blueprint('crud', __name__)

@bp.route('/employees', methods=['GET'])
def employees():
    db = get_db()
    employees_list = db.execute('SELECT * FROM employees;').fetchall()

    return make_response(json.dumps([dict(row) for row in employees_list]), 200)