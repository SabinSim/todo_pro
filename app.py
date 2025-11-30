from flask import Flask
from todo.routes import todo_bp
from auth.routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "sabin_secret"

    # Blueprint 등록
    app.register_blueprint(todo_bp, url_prefix="/todos")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
