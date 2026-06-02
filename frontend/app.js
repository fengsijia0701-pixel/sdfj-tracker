// SDFJ Tracker Frontend

const API_BASE = '/api';
let allArtists = [];
let selectedArtistId = null;

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    loadArtists();
    setupEventListeners();
});

// 事件监听
function setupEventListeners() {
    document.getElementById('generationFilter').addEventListener('change', filterArtists);
    document.getElementById('platformFilter').addEventListener('change', filterArtists);
    document.getElementById('refreshBtn').addEventListener('click', () => {
        loadArtists();
        loadRecentDynamics();
    });
}

// 加载艺人列表
async function loadArtists() {
    try {
        const response = await fetch(`${API_BASE}/artists`);
        allArtists = await response.json();
        updateStats();
        filterArtists();
    } catch (error) {
        console.error('加载艺人失败:', error);
        document.getElementById('artistsGrid').innerHTML =
            '<p class="loading">加载失败，请刷新重试</p>';
    }
}

// 更新统计
function updateStats() {
    document.getElementById('artistCount').textContent = allArtists.length;
    document.getElementById('lastUpdate').textContent = new Date().toLocaleTimeString('zh-CN');
}

// 筛选艺人
function filterArtists() {
    const generation = document.getElementById('generationFilter').value;
    const platform = document.getElementById('platformFilter').value;

    let filtered = allArtists;
    if (generation) {
        filtered = filtered.filter(a => a.generation === parseInt(generation));
    }

    renderArtists(filtered);
    document.getElementById('dynamicCount').textContent = filtered.length;
}

// 渲染艺人列表
function renderArtists(artists) {
    const grid = document.getElementById('artistsGrid');

    if (artists.length === 0) {
        grid.innerHTML = '<p class="loading">暂无艺人</p>';
        return;
    }

    grid.innerHTML = artists.map(artist => `
        <div class="artist-card" onclick="selectArtist('${artist.id}')">
            <h3>${artist.name}</h3>
            <p class="group">${artist.group}</p>
            <span class="generation-badge">第${artist.generation}代</span>
        </div>
    `).join('');
}

// 选择艺人
async function selectArtist(artistId) {
    selectedArtistId = artistId;
    await loadArtistDynamics(artistId);
}

// 加载艺人动态
async function loadArtistDynamics(artistId) {
    const platform = document.getElementById('platformFilter').value;
    let url = `${API_BASE}/artists/${artistId}/dynamics?limit=20`;
    if (platform) url += `&platform=${platform}`;

    try {
        const response = await fetch(url);
        const dynamics = await response.json();
        renderDynamics(dynamics);
    } catch (error) {
        console.error('加载动态失败:', error);
    }
}

// 加载最近动态
async function loadRecentDynamics() {
    try {
        const response = await fetch(`${API_BASE}/dynamics/recent?limit=20`);
        const dynamics = await response.json();
        if (selectedArtistId === null) {
            renderDynamics(dynamics);
        }
    } catch (error) {
        console.error('加载动态失败:', error);
    }
}

// 渲染动态列表
function renderDynamics(dynamics) {
    const list = document.getElementById('dynamicsList');

    if (dynamics.length === 0) {
        list.innerHTML = '<p class="loading">暂无动态数据</p>';
        return;
    }

    list.innerHTML = dynamics.map(d => `
        <div class="dynamic-item">
            <p class="platform">${getPlatformName(d.platform)} · ${formatTime(d.posted_at)}</p>
            <p class="content">${d.content || '暂无文字内容'}</p>
            <p class="meta">👍 ${d.likes_count} · 💬 ${d.comments_count} · 🔁 ${d.reposts_count}</p>
        </div>
    `).join('');
}

// 平台名称
function getPlatformName(platform) {
    const names = {
        weibo: '微博',
        bilibili: '哔哩哔哩',
        douban: '豆瓣',
        news: '新闻'
    };
    return names[platform] || platform;
}

// 格式化时间
function formatTime(datetime) {
    if (!datetime) return '--';
    const date = new Date(datetime);
    return date.toLocaleString('zh-CN');
}
