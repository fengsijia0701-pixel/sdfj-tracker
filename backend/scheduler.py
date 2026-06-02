# 定时任务模块

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime
from backend.models import load_artists
from backend.scrapers import fetch_bilibili_artist_videos, search_artist_bilibili
from backend.scrapers.news import fetch_artist_news
from backend.models.dynamics import save_dynamics

scheduler = AsyncIOScheduler()


async def fetch_all_artists_data():
    """抓取所有艺人的数据"""
    print(f"[{datetime.now().isoformat()}] 开始抓取所有艺人数据...")
    artists = load_artists()

    total_saved = 0
    for artist in artists:
        try:
            # 抓取 B站视频
            videos = fetch_bilibili_artist_videos(artist)
            if videos:
                saved = save_dynamics(videos)
                total_saved += saved
                print(f"  {artist.name}: 保存 {saved} 条B站视频")

            # 抓取新闻
            news = fetch_artist_news(artist)
            if news:
                saved = save_dynamics(news)
                total_saved += saved
                print(f"  {artist.name}: 保存 {saved} 条新闻")
        except Exception as e:
            print(f"  {artist.name}: 抓取失败 - {e}")

    print(f"[{datetime.now().isoformat()}] 抓取完成，共保存 {total_saved} 条动态")


def start_scheduler():
    """启动定时任务调度器"""
    # 每 6 小时抓取一次
    scheduler.add_job(
        fetch_all_artists_data,
        trigger=IntervalTrigger(hours=6),
        id="fetch_all_data",
        name="抓取所有艺人数据",
        replace_existing=True,
    )

    scheduler.start()
    print("定时任务调度器已启动 (每 6 小时执行一次)")


def stop_scheduler():
    """停止定时任务调度器"""
    scheduler.shutdown()
    print("定时任务调度器已停止")
