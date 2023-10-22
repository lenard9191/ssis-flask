from flask import Flask
from .extension import mysql
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    mysql.init_app(app)

    # Import parts of our application
    from .routes import college, course, student
    
    # Register Blueprints
    app.register_blueprint(college.college_bp)
    app.register_blueprint(course.course_bp)
    app.register_blueprint(student.student_bp)
    

    return app

