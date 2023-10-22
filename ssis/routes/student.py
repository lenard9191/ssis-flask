from flask import Blueprint
from flask import current_app as app
from flask import render_template, request, redirect, url_for, jsonify

from ..models.Course import Course
from ..models.College import College
from ..models.Student import Student
student_bp = Blueprint(
    "student_bp",
    __name__,
)

@student_bp.route("/")
@student_bp.route("/student")
def student():
    return render_template('student_home.html')