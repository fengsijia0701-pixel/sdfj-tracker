# SDFJ Tracker - 时代峰峻艺人动向收集器

> 追踪一代到四代艺人的最新动态

## 功能特点

- 📋 **艺人列表** — 按代际分组，展示所有追踪艺人
- 📰 **动态时间线** — 每个艺人的最新动态，按时间倒序排列
- 🔍 **多维度筛选** — 按代际、平台、内容类型快速筛选
- ⏰ **定时自动抓取** — 每 6 小时自动更新艺人动态
- 📊 **热度统计** — 简单统计各平台动态数量和趋势

## 艺人覆盖

| 代际 | 组合/班级 | 成员 |
|------|-----------|------|
| 一代 | TFBOYS | 王俊凯、王源、易烊千玺 |
| 二代 | 时代少年团 | 马嘉祺、丁程鑫、宋亚轩、刘耀文、张真源、严浩翔、贺峻霖 |
| 三代 | TOP登陆少年 / TF_ING | 朱志鑫、苏新皓、张极、张泽禹、左航 等 12 人 |
| 四代 | 一班 / 二班 | 陈浚铭、张桂源 等 15 人 |

**总计：37 位艺人**

## 技术栈

- **后端**: Python 3.14 + FastAPI + SQLite
- **前端**: HTML/CSS/JS（无框架）
- **定时任务**: APScheduler
- **搜索辅助**: MCP duckduckgo-search
- **包管理**: uv

## 快速开始

### 1. 安装依赖

```bash
uv sync
```

### 2. 初始化数据库

```bash
uv run python backend/database.py
```

### 3. 启动服务

```bash
uv run uvicorn backend.main:app --reload
```

### 4. 打开浏览器

访问 http://localhost:8000

## 项目结构

```
sdfj-tracker/
├── backend/
│   ├── main.py              # FastAPI 入口
│   ├── database.py          # 数据库初始化
│   ├── scheduler.py         # 定时任务
│   ├── models/               # 数据模型
│   │   ├── artist.py        # 艺人模型
│   │   ├── dynamic.py       # 动态模型
│   │   └── ...
│   ├── scrapers/            # 抓取模块
│   │   ├── bilibili.py      # B站抓取
│   │   └── news.py          # 新闻抓取
│   └── api/                 # API 路由
│       └── routes.py
├── frontend/                 # 前端看板
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── data/
│   ├── artists.json         # 艺人数据
│   └── database.sqlite      # SQLite 数据库
├── pyproject.toml
└── README.md
```

## API 端点

| 端点 | 方法 | 说明 |
|------|------|------|
| `GET /api/artists` | GET | 获取艺人列表 |
| `GET /api/artists/{id}` | GET | 获取单个艺人 |
| `GET /api/artists/{id}/dynamics` | GET | 获取艺人动态 |
| `GET /api/dynamics/recent` | GET | 获取最新动态 |

## 数据抓取

### 当前状态

- B站抓取模块：占位实现（需要 API 权限）
- 新闻抓取模块：占位实现（需要 MCP 搜索集成）

### 待实现

- [ ] B站官方 API 集成
- [ ] 微博 API 集成
- [ ] MCP duckduckgo-search 集成
- [ ] WebFetch 新闻页面抓取

## 开发说明

### 添加新艺人

编辑 `data/artists.json`，添加新的艺人数据。

### 修改抓取逻辑

- B站抓取: `backend/scrapers/bilibili.py`
- 新闻抓取: `backend/scrapers/news.py`

### 修改定时频率

编辑 `backend/scheduler.py` 中的 `IntervalTrigger(hours=6)`。

## 注意事项

1. **API 权限**: 微博/B站官方 API 需要申请，部分需要企业认证
2. **反爬机制**: 注意控制请求频率，避免被封
3. **数据存储**: 长期运行后数据库会增长，可设置定期清理

## License

MIT
