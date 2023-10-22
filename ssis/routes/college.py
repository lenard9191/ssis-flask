from flask import Blueprint
from flask import current_app as app
from flask import render_template , request, redirect, url_for, session
from ..models.College import College

college_bp = Blueprint(
    "college_bp",
    __name__,
)

@college_bp.route("/")
@college_bp.route("/college")
def college():
    return render_template('college_home.html')