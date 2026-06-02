# 艺人数据模型

from pydantic import BaseModel, Field
from typing import Optional


class Artist(BaseModel):
    """艺人数据模型"""
    id: str = Field(..., description="艺人唯一标识符")
    name: str = Field(..., description="艺人姓名")
    generation: int = Field(..., description="代际 (1-4)")
    group: str = Field(..., description="所属组合/班级")
    group_type: str = Field(..., description="组合类型: TFBOYS/时代少年团/TOP登陆少年/TF_ING/一班/二班")

    # 社交媒体账号
    weibo_uid: Optional[str] = Field(None, description="微博 UID")
    bilibili_id: Optional[str] = Field(None, description="B站 ID")

    # 状态
    is_active: bool = Field(True, description="是否活跃")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "wangjunkai",
                "name": "王俊凯",
                "generation": 1,
                "group": "TFBOYS",
                "group_type": "TFBOYS",
                "weibo_uid": "1234567890",
                "bilibili_id": "12345678",
                "is_active": True
            }
        }
