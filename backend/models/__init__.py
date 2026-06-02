# 后端数据模型

from backend.models.artist import Artist
from backend.models.dynamic import Dynamic
from backend.models.artists import load_artists, get_artist_by_id, get_artists_by_generation, get_artists_by_group
from backend.models.dynamics import save_dynamic, save_dynamics, get_dynamics_by_artist

__all__ = [
    "Artist",
    "Dynamic",
    "load_artists",
    "get_artist_by_id",
    "get_artists_by_generation",
    "get_artists_by_group",
    "save_dynamic",
    "save_dynamics",
    "get_dynamics_by_artist",
]
