from datetime import datetime
from .models import get_conn

def get_todos(user_id):
    conn = get_conn()
    # 내 할 일만 조회 (인증 기반 시스템의 핵심)
    rows = conn.execute("SELECT * FROM todos WHERE user_id = ? ORDER BY done ASC, id DESC", (user_id,)).fetchall()
    conn.close()
    return rows

def get_todo(id, user_id):
    conn = get_conn()
    # 수정/삭제 시 남의 글을 건드리지 못하게 user_id 체크
    row = conn.execute("SELECT * FROM todos WHERE id = ? AND user_id = ?", (id, user_id)).fetchone()
    conn.close()
    return row

def create_todo(user_id, title, desc, priority, category, deadline):
    conn = get_conn()
    conn.execute("""
        INSERT INTO todos (user_id, title, description, priority, category, deadline, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, title, desc, priority, category, deadline, datetime.now().strftime("%Y-%m-%d")))
    conn.commit()
    conn.close()

def update_todo(id, user_id, title, desc, priority, category, deadline):
    conn = get_conn()
    conn.execute("""
        UPDATE todos SET title=?, description=?, priority=?, category=?, deadline=?
        WHERE id=? AND user_id=?
    """, (title, desc, priority, category, deadline, id, user_id))
    conn.commit()
    conn.close()

def toggle_done(id, user_id):
    conn = get_conn()
    # 현재 상태를 조회해서 반대로 뒤집음 (0->1, 1->0)
    conn.execute("""
        UPDATE todos SET done = CASE WHEN done = 0 THEN 1 ELSE 0 END 
        WHERE id = ? AND user_id = ?
    """, (id, user_id))
    conn.commit()
    conn.close()

def delete_todo(id, user_id):
    conn = get_conn()
    conn.execute("DELETE FROM todos WHERE id = ? AND user_id = ?", (id, user_id))
    conn.commit()
    conn.close()

# 기존 코드 아래에 추가하세요

def get_todo_stats(user_id):
    conn = get_conn()
    
    # 1. 전체 할 일 수
    total = conn.execute("SELECT COUNT(*) FROM todos WHERE user_id = ?", (user_id,)).fetchone()[0]
    
    # 2. 완료된 할 일 수
    done_count = conn.execute("SELECT COUNT(*) FROM todos WHERE user_id = ? AND done = 1", (user_id,)).fetchone()[0]
    
    # 3. 미완료된 할 일 수
    pending_count = total - done_count

    # 4. 카테고리별 할 일 수 (많은 순서대로)
    categories = conn.execute("""
        SELECT category, COUNT(*) as count
        FROM todos 
        WHERE user_id = ? AND category IS NOT NULL AND category != ''
        GROUP BY category
        ORDER BY count DESC
    """, (user_id,)).fetchall()

    conn.close()
    
    return {
        'total': total,
        'done_count': done_count,
        'pending_count': pending_count,
        'categories': categories
    }