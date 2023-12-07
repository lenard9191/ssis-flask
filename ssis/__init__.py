from flask import Flask
from .extension import mysql
from config import Config
import cloudinary

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    mysql.init_app(app)

    # Cloudinary
    cloudinary.config(
        cloud_name=Config.CLOUDINARY_CLOUD_NAME,
        api_key=Config.CLOUDINARY_API_KEY,
        api_secret=Config.CLOUDINARY_API_SECRET,
        folder=Config.CLOUDINARY_FOLDER,
        secure=True
    )

    # Import parts of our application
    from .routes import college, course, student
    
    # Register Blueprints
    app.register_blueprint(college.college_bp)
    app.register_blueprint(course.course_bp)
    app.register_blueprint(student.student_bp)
    

    return app

