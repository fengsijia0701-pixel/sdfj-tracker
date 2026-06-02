# 数据库初始化与连接管理

import sqlite3
from pathlib import Path
from contextlib import contextmanager
from typing import Generator

DATABASE_PATH = Path(__file__).parent.parent / "data" / "database.sqlite"


def get_connection() -> sqlite3.Connection:
    """获取数据库连接"""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@contextmanager
def get_db() -> Generator[sqlite3.Connection, None, None]:
    """数据库上下文管理器"""
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_database() -> None:
    """初始化数据库表结构"""
    with get_db() as conn:
        cursor = conn.cursor()

        # 艺人表
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS artists (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                generation INTEGER NOT NULL,
                group_name TEXT NOT NULL,
                group_type TEXT NOT NULL,
                weibo_uid TEXT,
                bilibili_id TEXT,
                is_active INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # 动态/帖子表
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dynamics (
                id TEXT PRIMARY KEY,
                artist_id TEXT NOT NULL,
                platform TEXT NOT NULL,
                content_type TEXT NOT NULL,
                content TEXT,
                url TEXT,
                likes_count INTEGER DEFAULT 0,
                comments_count INTEGER DEFAULT 0,
                reposts_count INTEGER DEFAULT 0,
                posted_at TIMESTAMP,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (artist_id) REFERENCES artists(id)
            )
        """)

        # 创建索引
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_dynamics_artist_id
            ON dynamics(artist_id)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_dynamics_posted_at
            ON dynamics(posted_at DESC)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_dynamics_platform
            ON dynamics(platform)
        """)

        # 爬虫任务记录表
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fetch_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT NOT NULL,
                started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                status TEXT DEFAULT 'running',
                items_fetched INTEGER DEFAULT 0,
                error_message TEXT
            )
        """)

        conn.commit()

    print(f"数据库初始化完成: {DATABASE_PATH}")


if __name__ == "__main__":
    init_database()
