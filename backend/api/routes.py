# API 路由

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from backend.models import (
    load_artists,
    get_artist_by_id,
    get_artists_by_generation,
    get_dynamics_by_artist,
    Artist,
    Dynamic,
)

router = APIRouter()


@router.get("/artists", response_model=List[Artist])
async def get_artists(
    generation: Optional[int] = Query(None, description="按代际筛选"),
):
    """获取艺人列表，可选按代际筛选"""
    if generation:
        return get_artists_by_generation(generation)
    return load_artists()


@router.get("/artists/{artist_id}", response_model=Artist)
async def get_artist(artist_id: str):
    """获取单个艺人信息"""
    artist = get_artist_by_id(artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="艺人未找到")
    return artist


@router.get("/artists/{artist_id}/dynamics", response_model=List[Dynamic])
async def get_artist_dynamics(
    artist_id: str,
    limit: int = Query(50, ge=1, le=100, description="返回数量限制"),
    platform: Optional[str] = Query(None, description="按平台筛选"),
):
    """获取指定艺人的动态"""
    artist = get_artist_by_id(artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="艺人未找到")
    return get_dynamics_by_artist(artist_id, limit=limit, platform=platform)


@router.get("/dynamics/recent", response_model=List[Dynamic])
async def get_recent_dynamics(
    limit: int = Query(50, ge=1, le=100, description="返回数量限制"),
    platform: Optional[str] = Query(None, description="按平台筛选"),
):
    """获取最近的动态"""
    # TODO: 实现从数据库获取最新动态
    return []
