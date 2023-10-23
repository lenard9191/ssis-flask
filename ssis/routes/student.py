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
    colleges = College.get_all()
    courses = Course.get_all()
    students = Student.get_all()
    return render_template('student_home.html', colleges=colleges , courses=courses,students=students)


@student_bp.route("/student/add", methods=['POSt'])
def student_add():
    id = request.form.get('id')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    course_code = request.form.get('course_code')
    year = request.form.get('year')
    gender = request.form.get('gender')

    error = f"{id} {firstname} {lastname} {course_code} {year} {gender}"


    exist_student = Student.check_existing_id(id)

    if exist_student:
        error = f"Student ID: {id} is already taken"
        return jsonify({
            'error' : error
        })
    else :
        try:
            student = Student(id=id,firstname=firstname,lastname=lastname,course_code=course_code,year=year,gender=gender)
            student.add()
            return redirect(url_for("student_bp.student"))
        except Exception as e:
            return jsonify({
                'error' : e
            })
    