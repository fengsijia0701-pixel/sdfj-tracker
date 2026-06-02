# 艺人数据加载工具

import json
from pathlib import Path
from typing import List
from backend.models.artist import Artist


def load_artists() -> List[Artist]:
    """从 artists.json 加载所有艺人数据"""
    artists_file = Path(__file__).parent.parent.parent / "data" / "artists.json"
    with open(artists_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Artist(**artist) for artist in data["artists"]]


def get_artist_by_id(artist_id: str) -> Artist | None:
    """根据 ID 获取艺人"""
    artists = load_artists()
    for artist in artists:
        if artist.id == artist_id:
            return artist
    return None


def get_artists_by_generation(generation: int) -> List[Artist]:
    """获取指定代际的所有艺人"""
    artists = load_artists()
    return [a for a in artists if a.generation == generation]


def get_artists_by_group(group: str) -> List[Artist]:
    """获取指定组合的所有艺人"""
    artists = load_artists()
    return [a for a in artists if a.group == group]
