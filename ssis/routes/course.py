from flask import Blueprint
from flask import current_app as app
from flask import render_template, request, redirect, jsonify, url_for

from ..models.Course import Course
from ..models.College import College

course_bp = Blueprint(
    "course_bp",
    __name__,
)

@course_bp.route("/course", methods=['GET', 'POST'])
def course():
    return render_template('course_home.html')