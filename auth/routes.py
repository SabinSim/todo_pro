from flask import Blueprint, render_template, request, redirect, session, flash
from .services import create_user, find_user_by_username, verify_password

auth_bp = Blueprint("auth", __name__, template_folder="templates")

@auth_bp.route("/")
def home():
    if "user_id" in session:
        return redirect("/todos")
    return redirect("/login")

# ---------------------------------------------------------
# [중요] methods에 "GET"이 꼭 있어야 페이지가 보입니다!
# ---------------------------------------------------------
@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    # 데이터 제출(POST)일 때
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        
        if not username or not password:
            flash("아이디와 비밀번호를 모두 입력해주세요.", "danger")
            return render_template("auth/signup.html")
        
        if find_user_by_username(username):
            flash("이미 존재하는 아이디입니다.", "warning")
            return render_template("auth/signup.html")

        try:
            create_user(username, password)
            flash("가입이 완료되었습니다! 로그인해주세요.", "success")
            return redirect("/login")
        except:
            flash("회원가입 중 오류가 발생했습니다.", "danger")
            return render_template("auth/signup.html")

    # 페이지 접속(GET)일 때
    return render_template("auth/signup.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = find_user_by_username(username)

        if user and verify_password(user["password"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            flash(f"반가워요, {user['username']}님!", "success")
            return redirect("/todos")
        
        flash("아이디 또는 비밀번호가 올바르지 않습니다.", "danger")
        return render_template("auth/login.html")

    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("로그아웃 되었습니다.", "info")
    return redirect("/login")