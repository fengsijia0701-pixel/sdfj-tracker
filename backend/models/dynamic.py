# 动态数据模型

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Dynamic(BaseModel):
    """艺人动态数据模型"""
    id: str = Field(..., description="动态唯一标识符")
    artist_id: str = Field(..., description="艺人ID")
    platform: str = Field(..., description="平台: weibo/bilibili/douban/news")

    # 内容类型
    content_type: str = Field(..., description="内容类型: post/video/activity/news")

    # 内容
    content: Optional[str] = Field(None, description="动态文字内容")
    url: Optional[str] = Field(None, description="原文链接")

    # 互动数据
    likes_count: int = Field(0, description="点赞数")
    comments_count: int = Field(0, description="评论数")
    reposts_count: int = Field(0, description="转发数")

    # 时间
    posted_at: Optional[datetime] = Field(None, description="发布时间")
    fetched_at: datetime = Field(default_factory=datetime.now, description="抓取时间")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "weibo_1234567890",
                "artist_id": "wangjunkai",
                "platform": "weibo",
                "content_type": "post",
                "content": "这是一条微博内容",
                "url": "https://weibo.com/1234567890",
                "likes_count": 10000,
                "comments_count": 500,
                "reposts_count": 200,
                "posted_at": "2026-06-03T10:00:00",
                "fetched_at": "2026-06-03T12:00:00"
            }
        }
