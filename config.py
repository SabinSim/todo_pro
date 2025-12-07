import os

# 현재 파일(config.py)이 있는 위치를 기준점으로 잡음
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    # 환경변수에서 키를 가져오거나, 없으면 기본값 사용
    SECRET_KEY = os.environ.get('SECRET_KEY') or "sabin_todo_pro_secret_key"
    
    # DB 파일 경로를 절대 경로로 고정 (중요!)
    DATABASE = os.path.join(BASE_DIR, 'todo_pro.db')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False