from os import getenv

class Config:
    # FLASK

    FLASK_APP = getenv("FLASK_APP")
    FLASK_DEBUG = getenv("FLASK_DEBUG")

    # IDK??  
    
    
    # DataBase ASSETS
    SECRET_KEY = getenv("SECRET_KEY")
    MYSQL_DB = getenv("DB_NAME")
    MYSQL_USER = getenv("DB_USERNAME")
    MYSQL_PASSWORD = getenv("DB_PASSWORD")
    MYSQL_HOST = getenv("DB_HOST")
    MYSQL_PORT = int(getenv("DB_PORT"))

    # Cloudinary

    CLOUDINARY_CLOUD_NAME = getenv('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_API_KEY = getenv('CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET = getenv('CLOUDINARY_API_SECRET')
    CLOUDINARY_FOLDER = getenv('CLOUDINARY_FOLDER')
