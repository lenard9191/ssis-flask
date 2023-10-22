from flask import Blueprint
from flask import current_app as app
from flask import render_template , request, redirect, url_for, session
from ..models.College import College

college_bp = Blueprint(
    "college_bp",
    __name__,
)

@college_bp.route("/college")
def college():
    colleges = College.get_all()
    return render_template('college_home.html', colleges=colleges)

@college_bp.route("/college/search", methods=['GET','POST'])
def college_search():
    input = request.args.get("querycollege")
    filter = request.args.get("filter_college")
    if input:
        colleges = College.search(input,filter)
        if not colleges:
            filter_message = ""
            if filter == "0":
                filter_message = "College Code or College name"
            elif filter == "1":
                filter_message = "College Code"
            elif filter == "2":
                filter_message = "College name"
            return render_template('college_home.html', collegeInput = input, search = True, hideAdd = True, filter_message=filter_message)
        else:
            return render_template('college_home.html', colleges=colleges, collegeInput = input , hideAdd=True,search = True)
    return redirect(url_for('college_bp.college'))