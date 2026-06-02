# 资讯抓取模块

from typing import List
from backend.models.artist import Artist
from backend.models.dynamic import Dynamic


def fetch_artist_news(artist: Artist, limit: int = 10) -> List[Dynamic]:
    """
    抓取指定艺人的新闻资讯

    使用 MCP duckduckgo-search 搜索新闻
    """
    # TODO: 实现真实的新闻搜索和抓取
    # 使用 MCP ddg-search 搜索艺人相关新闻
    # 使用 WebFetch 抓取新闻页面内容
    return []


def search_artist_mentions(artist: Artist, limit: int = 20) -> List[Dynamic]:
    """
    搜索艺人的全网提及
    """
    # TODO: 使用 MCP 搜索实现
    return []


if __name__ == "__main__":
    from backend.models import load_artists

    artists = load_artists()
    print(f"已加载 {len(artists)} 位艺人")

    # 测试抓取
    for artist in artists[:2]:
        news = fetch_artist_news(artist)
        print(f"{artist.name}: 获取到 {len(news)} 条新闻")
