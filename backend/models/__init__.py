# 后端数据模型

from backend.models.artist import Artist
from backend.models.artists import load_artists, get_artist_by_id, get_artists_by_generation, get_artists_by_group

__all__ = [
    "Artist",
    "load_artists",
    "get_artist_by_id",
    "get_artists_by_generation",
    "get_artists_by_group",
]
