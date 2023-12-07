from flask import Blueprint
from flask import current_app as app
from flask import render_template, request, redirect, url_for, jsonify

from ..models.Course import Course
from ..models.College import College
from ..models.Student import Student

from cloudinary import uploader
from cloudinary.uploader import upload
from config import Config
import re

student_bp = Blueprint(
    "student_bp",
    __name__,
)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def get_public_id_from_url(url):
    match = re.search(r'/v\d+/(ssis/[^/]+)\.\w+', url)
    return match.group(1) if match else None

def check_file_size(picture):
    maxsize = 1 * 1024 * 1024

    if picture and picture.content_length > 0 and picture.content_length <= maxsize:
        return True
    else:
        return False

@student_bp.route("/")
@student_bp.route("/student")
def student():
    colleges = College.get_all()
    courses = Course.get_all()
    students = Student.get_all()
    return render_template('student_home.html', colleges=colleges , courses=courses,students=students)


@student_bp.route("/student/add", methods=['POST'])
def student_add():
    id = request.form.get('student_id')
    firstname = request.form.get('student_first_name')
    lastname = request.form.get('student_last_name')
    course_code = request.form.get('student_course_code')
    year = request.form.get('student_year')
    gender = request.form.get('student_gender')
    picture = request.files['formFile']

    error = f"{id} {firstname} {lastname} {course_code} {year} {gender} {picture.filename}"

    exist_student = Student.check_existing_id(id)

    if exist_student:
        error = f"Student ID: {id} is already taken"
        return jsonify({
            'error' : error
        })
    else :
        try:
            student = Student(id=id,firstname=firstname,lastname=lastname,course_code=course_code,year=year,gender=gender)
            if not check_file_size(picture):
                return jsonify({'error': 'Max Size Limit is: 1mb' })
            if picture and allowed_file(picture.filename):
                result = upload(picture, folder= Config.CLOUDINARY_FOLDER)
                student.picture = result['secure_url']
            else :
                return jsonify({ 'error': 'Image is required and pictures only'})
            student.add()
            return redirect(url_for("student_bp.student"))
        except Exception as e:
            return jsonify({
                'error' : e
            })
    

@student_bp.route("/student/delete", methods=['POST'])
def student_delete():
    try:
        id = request.form.get('csasdsda')
        student = Student.get_one(id)
        if student.picture:
            public_id = get_public_id_from_url(student.picture)
            result = uploader.destroy(public_id)
        student.delete()
        return redirect(url_for("student_bp.student"))
    except Exception as e:
        error = f"Error: {e}"
        return jsonify({
            'error' : error
        })


@student_bp.route("/student/edit", methods=['POST'])
def student_edit():
    pastid = request.form.get('pastid')
    id = request.form.get('edit_student_id')
    firstname = request.form.get('edit_student_first_name')
    lastname = request.form.get('edit_student_last_name')
    course_code = request.form.get('edit_student_course_code')
    year = request.form.get('edit_student_year')
    gender = request.form.get('edit_student_gender')
    picture = request.files['editFormFile']

    error = f"{pastid} {id} {firstname} {lastname} {course_code} {year} {gender} {picture.filename}"

    student = Student.get_one(pastid)
    if id != pastid:
        exist_student = Student.get_one(id)
        if exist_student:
            error = f"Student ID: {id} is already taken"
            return jsonify({'error' : error})
        else:
            try:
                student = Student(id=id,firstname=firstname,lastname=lastname,course_code=course_code,year=year,gender=gender)
                if not check_file_size(picture):
                    return jsonify({'error': 'Max Size Limit is: 1mb' })
                if picture and allowed_file(picture.filename):
                    if student.picture:
                        public_id = get_public_id_from_url(student.picture)
                        result = uploader.destroy(public_id)
                    result1 = upload(picture, folder= Config.CLOUDINARY_FOLDER)
                    student.picture = result1['secure_url']
                elif not picture and not student.picture :
                    return jsonify({ 'error': 'Image is required and pictures only'})
                student.update(pastid)
                return redirect(url_for("student_bp.student"))
            except Exception as e:
                return jsonify({'error': e})
    else:
        try:
            student.firstname = firstname
            student.lastname = lastname
            student.course_code = course_code
            student.year = year
            student.gender = gender
            if not check_file_size(picture):
                return jsonify({'error': 'Max Size Limit is: 1mb or 1024kb' })
            if picture and allowed_file(picture.filename):
                if student.picture:
                    public_id = get_public_id_from_url(student.picture)
                    result = uploader.destroy(public_id)
                result1 = upload(picture, folder= Config.CLOUDINARY_FOLDER)
                student.picture = result1['secure_url']
            elif not picture and not student.picture :
                return jsonify({ 'error': 'Image is required and pictures only'})
            student.update(id)
            return redirect(url_for("student_bp.student"))
        except Exception as e:
            return jsonify({'error' : e})
        

@student_bp.route("/student/search", methods=['GET','POST'])
def student_search():
    input = request.args.get('querystudent')
    filter = request.args.get('filter_student')

    if input:
        students = Student.search(input,filter)
        if not students:
            filter_message = ""
            if filter == "0":
                filter_message = "Student ID or NAME or COURSE or YEAR or GENDER"
            elif filter == "1":
                filter_message = "Student ID"
            elif filter == "2":
                filter_message = "Student FirstName"
            elif filter == "3":
                filter_message = "Student Last Name"
            elif filter == "4":
                filter_message= "Student Course"
            elif filter == "5":
                filter_message= "Student Year"
            elif filter == "6":
                filter_message = "Student Gender"
            return render_template('student_home.html', studentInput = input, search = True, hideAdd = True , filter_message=filter_message)
        else:
            return render_template('student_home.html', students=students, hideAdd = True, search = True, studentInput=input)
    return redirect(url_for("student_bp.student"))