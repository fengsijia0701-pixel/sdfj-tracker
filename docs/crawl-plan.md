# 时代峰峻艺人动向收集器 - 爬取方案

> 更新日期：2026-06-03

---

## 一、爬取优先级

| 优先级 | 平台 | 说明 |
|--------|------|------|
| 1 | 微博 | 用户确认优先，有账号资源 |
| 2 | B站 | 视频内容为主 |
| 3 | 新闻/资讯 | MCP 搜索补充 |

---

## 二、微博爬取方案

### 2.1 方案选择：移动端 API（推荐）

**接口地址**：`https://m.weibo.cn/api/container/getIndex`

**可获取数据**：
- 用户微博列表（正文、发布时间）
- 点赞数、评论数、转发数
- 微博评论区内容

**请求方式**：
```
GET https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&containerid=107603{uid}
Headers:
  User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)
  Cookie: {你的账号Cookie}
```

**频率限制**：
- 正常：60次/分钟
- 触发验证码：需等待或降低频率

---

### 2.2 Cookie 获取流程

1. 浏览器登录微博（m.weibo.cn）
2. 打开开发者工具（F12）→ Network
3. 找到任意 API 请求 → 复制 Request Headers 中的 Cookie
4. 将 Cookie 填入配置文件

---

### 2.3 艺人微博 UID 映射

37 位艺人需要映射微博 UID，可通过以下方式获取：

1. **搜索艺人微博主页** → URL 中的 uid 参数
2. **艺人官方微博**（部分艺人有官方账号）
3. **预留字段** — 在 artists.json 中预置 weibo_uid 字段

---

### 2.4 备选方案：搜狗微信搜索

**网址**：`https://weixin.sogou.com/`

- 优点：无需登录，可搜索公众号文章
- 缺点：只能搜到部分内容

---

## 三、B站爬取方案

### 3.1 方案选择：搜索 + WebFetch（Phase 1）

**流程**：
1. MCP duckduckgo-search 搜索艺人相关 B站视频
2. WebFetch 抓取视频页面获取播放/点赞数据
3. 解析 b23.tv 短链接获取完整信息

---

### 3.2 B站移动端 API（Phase 2）

**接口地址**：`https://api.bilibili.com/x/space/arc/search`

**请求方式**：
```
GET https://api.bilibili.com/x/space/arc/search?mid={mid}&pn=1&jsonp=jsonp
Headers:
  User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)
  Cookie: {你的B站账号Cookie}
```

---

## 四、新闻/资讯爬取方案

### 4.1 MCP 搜索

使用 duckduckgo-mcp-server 搜索艺人相关新闻：

```python
# 搜索示例
"时代少年团 最新动态"
"王俊凯 今日消息"
```

### 4.2 WebFetch 补充抓取

搜索结果页面 → WebFetch 获取完整文章内容

---

## 五、频率限制与应对

### 微博
| 情况 | 应对措施 |
|------|----------|
| 正常访问 | 每次请求间隔 1-2 秒 |
| 触发验证码 | 停止 10-15 分钟，降低频率 |
| Cookie 失效 | 提示用户更新 Cookie |

### B站
| 情况 | 应对措施 |
|------|----------|
| 正常访问 | 每次请求间隔 2-3 秒 |
| 频繁限制 | 降低频率或切换 IP |
| Cookie 失效 | 提示用户更新 |

---

## 六、数据存储结构

### dynamics 表字段

| 字段 | 类型 | 说明 |
|------|------|------|
| id | TEXT | 唯一标识（平台_原始ID） |
| artist_id | TEXT | 艺人ID |
| platform | TEXT | weibo/bilibili/news |
| content_type | TEXT | post/video/activity |
| content | TEXT | 文字内容 |
| url | TEXT | 原文链接 |
| likes_count | INTEGER | 点赞数 |
| comments_count | INTEGER | 评论数 |
| reposts_count | INTEGER | 转发数 |
| posted_at | TIMESTAMP | 发布时间 |
| fetched_at | TIMESTAMP | 抓取时间 |

---

## 七、实现计划

### Phase 1：MCP 搜索方案（明天实现）
- [ ] MCP duckduckgo-search 集成
- [ ] 微博关键词搜索
- [ ] 搜索结果 WebFetch 抓取
- [ ] 数据解析入库

### Phase 2：移动端 API（账号测试）
- [ ] 获取账号 Cookie
- [ ] 移动端 API 封装
- [ ] 艺人 UID 映射表
- [ ] 频率限制处理

### Phase 3：数据展示
- [ ] 完善 API 返回
- [ ] 前端动态展示
- [ ] 筛选功能增强

---

## 八、需要用户提供的信息

- [ ] **微博 Cookie** — 用于移动端 API 抓取
- [ ] **B站 Cookie** — 可选，用于更完整数据
- [ ] **优先抓取的艺人** — 37位全抓还是先试点几位？

---

## 九、风险提示

1. **账号风险** — 频繁访问可能导致账号被限制，请勿使用主账号测试
2. **Cookie 过期** — 定期需要更新
3. **数据完整性** — 非官方 API 数据可能不完整

---

*文档版本：v1.0*
