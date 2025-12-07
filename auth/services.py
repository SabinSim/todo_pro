from werkzeug.security import generate_password_hash, check_password_hash
from todo.models import get_conn 

def create_user(username, password):
    conn = get_conn()
    cur = conn.cursor()
    try:
        # 비밀번호는 반드시 해싱하여 저장 (보안 필수)
        hashed_pw = generate_password_hash(password)
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        conn.commit()
    finally:
        conn.close()

def find_user_by_username(username):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    return row

def verify_password(stored_hash, password):
    return check_password_hash(stored_hash, password)