# 微博 Cookie 获取教程

> 适用：移动端 API 抓取微博数据

---

## 获取步骤

### 1. 打开微博移动版

用浏览器打开：**https://m.weibo.cn**

### 2. 登录你的账号

使用手机号 + 验证码登录（推荐）

### 3. 打开开发者工具

按 **F12** 打开浏览器开发者工具

### 4. 切换到 Network（网络）标签

### 5. 刷新页面

按 **F5** 刷新 m.weibo.cn

### 6. 找到 API 请求

在 Network 列表中找到 URL 包含 `api` 的请求，例如：
- `https://m.weibo.cn/api/container/getIndex?`
- `https://m.weibo.cn/feed/friends`

### 7. 点击该请求 → 查看 Headers

找到 **Request Headers** 部分

### 8. 复制 Cookie 值

找到 `Cookie:` 字段，**复制完整的 Cookie 字符串**

---

## 复制的 Cookie 示例

```
SUB=1234567890abcdef...; _T_WM=1234567890...; etc...
```

**注意**：
- Cookie 很长，需要完整复制
- 不要只复制一部分
- Cookie 以分号分隔多个值

---

## 验证 Cookie 是否有效

复制后发给我，我可以用这个 Cookie 测试 API 是否能正常获取数据。

---

## 注意事项

1. **使用小号测试** — 频繁访问可能触发验证码，建议用不常用的小号
2. **Cookie 会过期** — 通常几天到几周，过期后需要重新获取
3. **不要泄露 Cookie** — 谁拿到你的 Cookie 就能操作你的账号

---

## 如果遇到问题

### Q：找不到 Network 标签？
- 可能是开发者工具被隐藏了，尝试按 **F12** 或 **Ctrl+Shift+I**

### Q：Cookie 字段在哪？
- 滚动到 Request Headers 最下方，应该在 `Cookie:` 行

### Q：登录不了移动版？
- 可以尝试电脑版微博，然后找 API 请求
- 或者告诉我你遇到的具体问题

---

*最后更新：2026-06-03*
