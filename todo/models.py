import sqlite3
from flask import current_app

def get_conn():
    """DB 연결 객체 반환 (Row Factory 적용)"""
    # config에 설정된 DB 경로를 가져옴
    conn = sqlite3.connect(current_app.config['DATABASE'])
    # 딕셔너리처럼 컬럼명으로 데이터에 접근하게 설정
    conn.row_factory = sqlite3.Row
    return conn