from flask import Blueprint, render_template

todo_bp = Blueprint("todo", __name__, template_folder="templates")

@todo_bp.route("/")
def index():
    return render_template("todo/index.html")
