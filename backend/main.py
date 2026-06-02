# FastAPI 入口

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pathlib import Path
from backend.api.routes import router as api_router
from backend.database import init_database

# 初始化数据库
init_database()

app = FastAPI(
    title="时代峰峻艺人动向收集器",
    description="追踪一代到四代艺人的最新动态",
    version="0.1.0",
)

# 挂载 API 路由
app.include_router(api_router, prefix="/api")

# 静态文件服务
frontend_path = Path(__file__).parent.parent / "frontend"
if frontend_path.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")


@app.get("/")
async def root():
    """返回前端页面"""
    index_path = frontend_path / "index.html"
    if index_path.exists():
        return RedirectResponse(url="/static/index.html")
    return {"message": "SDFJ Tracker API", "docs": "/docs"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
