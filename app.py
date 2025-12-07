from flask import Flask
from auth.routes import auth_bp
from todo.routes import todo_bp
from config import DevelopmentConfig
from init_db import init_db

def create_app():
    app = Flask(__name__)
    
    # 1. 설정 로드
    app.config.from_object(DevelopmentConfig)

    # 2. DB 초기화 (앱 실행 시 테이블 자동 생성)
    init_db(app)

    # 3. Blueprint 등록 (기능별 라우트 분리)
    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(todo_bp, url_prefix="/todos")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)