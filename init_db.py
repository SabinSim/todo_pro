import sqlite3

def init_db(app):
    """앱 컨텍스트 안에서 DB 테이블을 생성합니다."""
    with app.app_context():
        db_path = app.config['DATABASE']
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        # 1. 사용자 테이블 (인증 시스템의 핵심)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

        # 2. 할 일 테이블 (users 테이블과 관계 형성)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL, -- 누가 작성했는지 식별
                title TEXT NOT NULL,
                description TEXT,
                priority INTEGER DEFAULT 1,
                category TEXT,
                deadline TEXT,
                done INTEGER DEFAULT 0,
                created_at TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)

        conn.commit()
        conn.close()
        print(f"✅ DB 초기화 완료: {db_path}")