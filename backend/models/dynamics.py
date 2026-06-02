# 动态数据存储工具

from typing import List, Optional
from datetime import datetime
from backend.database import get_db
from backend.models.dynamic import Dynamic


def save_dynamic(dynamic: Dynamic) -> None:
    """保存单条动态到数据库"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO dynamics
            (id, artist_id, platform, content_type, content, url,
             likes_count, comments_count, reposts_count, posted_at, fetched_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            dynamic.id,
            dynamic.artist_id,
            dynamic.platform,
            dynamic.content_type,
            dynamic.content,
            dynamic.url,
            dynamic.likes_count,
            dynamic.comments_count,
            dynamic.reposts_count,
            dynamic.posted_at.isoformat() if dynamic.posted_at else None,
            dynamic.fetched_at.isoformat() if dynamic.fetched_at else None,
        ))
        conn.commit()


def save_dynamics(dynamics: List[Dynamic]) -> int:
    """批量保存动态，返回保存数量"""
    count = 0
    for d in dynamics:
        save_dynamic(d)
        count += 1
    return count


def get_dynamics_by_artist(
    artist_id: str,
    limit: int = 50,
    platform: Optional[str] = None
) -> List[Dynamic]:
    """获取指定艺人的动态"""
    with get_db() as conn:
        cursor = conn.cursor()
        if platform:
            cursor.execute("""
                SELECT * FROM dynamics
                WHERE artist_id = ? AND platform = ?
                ORDER BY posted_at DESC
                LIMIT ?
            """, (artist_id, platform, limit))
        else:
            cursor.execute("""
                SELECT * FROM dynamics
                WHERE artist_id = ?
                ORDER BY posted_at DESC
                LIMIT ?
            """, (artist_id, limit))
        rows = cursor.fetchall()
        return [_row_to_dynamic(row) for row in rows]


def _row_to_dynamic(row) -> Dynamic:
    """将数据库行转换为 Dynamic 对象"""
    return Dynamic(
        id=row["id"],
        artist_id=row["artist_id"],
        platform=row["platform"],
        content_type=row["content_type"],
        content=row["content"],
        url=row["url"],
        likes_count=row["likes_count"],
        comments_count=row["comments_count"],
        reposts_count=row["reposts_count"],
        posted_at=datetime.fromisoformat(row["posted_at"]) if row["posted_at"] else None,
        fetched_at=datetime.fromisoformat(row["fetched_at"]) if row["fetched_at"] else None,
    )
