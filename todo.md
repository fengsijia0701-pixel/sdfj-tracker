# 时代峰峻艺人动向收集器 - 待办事项

**项目：** fengjian-tracker  
**创建日期：** 2026-06-03  
**状态：** 进行中

---

## 待完成 Task

### 第一阶段：项目初始化与基础数据模型

- [ ] **Task 1: 项目结构与依赖**
  - 创建 pyproject.toml
  - 初始化 uv 项目
  - 创建目录结构
  - 提交初始 commit

- [ ] **Task 2: 艺人数据模型**
  - 创建 artists.json（完整艺人数据）
  - 创建 Artist 数据类
  - 提交

- [ ] **Task 3: 数据库初始化**
  - 创建 database.py（SQLite 初始化）
  - 初始化数据库
  - 提交

### 第二阶段：数据抓取模块

- [ ] **Task 4: 动态数据模型**
  - 创建 Dynamic 数据类
  - 提交

- [ ] **Task 5: B站抓取模块**
  - 创建 bilibili.py
  - 提交

- [ ] **Task 6: 资讯抓取模块**
  - 创建 news.py（占位实现）
  - 提交

### 第三阶段：API 与看板

- [ ] **Task 7: API 路由**
  - 创建 routes.py
  - 创建 main.py
  - 提交

- [ ] **Task 8: 前端看板**
  - 创建 index.html
  - 创建 styles.css
  - 创建 app.js
  - 提交

- [ ] **Task 9: 定时任务模块**
  - 创建 scheduler.py
  - 更新 main.py
  - 提交

### 第四阶段：文档与 README

- [ ] **Task 10: README 与使用文档**
  - 创建 README.md
  - 提交

---

## 技术风险（高优先级）

1. ⚠️ API权限 — 微博/B站官方API需要申请
2. ⚠️ 反爬机制 — 需要控制请求频率
3. ⚠️ 登录态维护 — 部分数据需要登录态

---

## 技术风险（中优先级）

4. 🔄 数据一致性 — 不同平台数据格式不同
5. 🔄 存储成本 — 长期数据增长
6. 🔄 MCP 稳定性 — 依赖第三方服务