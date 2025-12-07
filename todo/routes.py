from flask import Blueprint, render_template, request, redirect, session, abort, flash
from datetime import datetime
from .services import (
    get_todos, create_todo, get_todo, update_todo, toggle_done, delete_todo, get_todo_stats
)

todo_bp = Blueprint("todo", __name__, template_folder="templates")

def login_required():
    if "user_id" not in session:
        return None
    return session["user_id"]

@todo_bp.route("/")
def index():
    user_id = login_required()
    if not user_id: return redirect("/login")

    todos = get_todos(user_id)
    return render_template("todo/index.html", todos=todos)

@todo_bp.route("/new")
def new_form():
    if not login_required(): return redirect("/login")
    return render_template("todo/new.html")

@todo_bp.route("/create", methods=["POST"])
def create():
    user_id = login_required()
    if not user_id: return redirect("/login")
    
    title = request.form.get("title", "").strip()
    deadline = request.form.get("deadline", "")
    
    # 4) 입력 폼 오류 처리
    if not title:
        flash("제목은 필수입니다!", "danger")
        return redirect("/todos/new")
    
    # 마감일 체크 (오늘 이전이면 경고)
    if deadline:
        today = datetime.now().strftime("%Y-%m-%d")
        if deadline < today:
            flash("마감일이 오늘보다 이전입니다. 그래도 등록했습니다.", "warning")

    create_todo(
        user_id,
        title,
        request.form.get("description"),
        request.form.get("priority", 1),
        request.form.get("category"),
        deadline
    )
    flash("할 일이 성공적으로 등록되었습니다.", "success")
    return redirect("/todos")

# ... (중간 코드: edit, update, toggle 등은 기존 유지) ...
# update 부분만 아래 코드로 바꿔주세요 (유효성 검사 추가됨)

@todo_bp.route("/edit/<int:id>")
def edit_form(id):
    user_id = login_required()
    if not user_id: return redirect("/login")

    todo = get_todo(id, user_id)
    if not todo: abort(404)
    return render_template("todo/edit.html", todo=todo)

@todo_bp.route("/update/<int:id>", methods=["POST"])
def update(id):
    user_id = login_required()
    if not user_id: return redirect("/login")
    
    title = request.form.get("title", "").strip()
    
    if not title:
        flash("제목을 비울 수 없습니다.", "danger")
        return redirect(f"/todos/edit/{id}")

    update_todo(
        id, user_id,
        title,
        request.form.get("description"),
        request.form.get("priority", 1),
        request.form.get("category"),
        request.form.get("deadline")
    )
    flash("수정이 완료되었습니다.", "success")
    return redirect("/todos")

@todo_bp.route("/toggle/<int:id>")
def toggle(id):
    user_id = login_required()
    if not user_id: return redirect("/login")
    toggle_done(id, user_id)
    return redirect("/todos")

@todo_bp.route("/delete/<int:id>")
def delete(id):
    user_id = login_required()
    if not user_id: return redirect("/login")
    delete_todo(id, user_id)
    flash("할 일이 삭제되었습니다.", "info")
    return redirect("/todos")

@todo_bp.route("/stats")
def stats():
    user_id = login_required()
    if not user_id: return redirect("/login")
    
    stats_data = get_todo_stats(user_id)
    return render_template("todo/stats.html", stats=stats_data)