# 广东高考投档分数线查询工具（本科+专科）

基于 2023-2025 年广东省高考投档数据的 Web 查询工具，包含本科和专科全部数据。

## 数据来源

- **投档数据**：广东省教育考试院 2023-2025 年普通类投档情况 PDF（本科+专科）
- **办学性质**：中国教育在线（eol.cn）院校数据库
- **数据量**：20,392 条记录（本科 13,998 + 专科 6,394），覆盖 1,700+ 所院校

## 功能

- 按层次筛选（本科/专科/全部）
- 按年份筛选（2023/2024/2025/全部）
- 按科类筛选（历史/物理/全部）
- 按办学性质筛选（公办/民办/中外合作/独立学院/港澳台合作/境外办学/全部）
- **省份动态筛选**：从数据中自动提取，支持全部 33 个省份/地区
- **院校代码精确搜索**：输入院校代码精确查找
- **院校名称模糊搜索**：输入关键词模糊匹配
- **排位区间筛选**：最低排位 ~ 最高排位范围查询
- **分数区间筛选**：最低分 ~ 最高分范围查询
- 结果排序（点击年份/院校代码/计划数/录取人数/录取最低分/录取最低排位）
- **表头固定**：向下滚动时表头固定在视口顶部
- **分页加载**：每页 500 条，避免大数据量卡顿
- **导出 Excel**（蓝底白字表头、冻结首行、自动列宽）
- 响应式布局，支持移动端

## 快速部署

### Docker Compose（推荐）

```bash
docker compose up -d
```

访问 http://localhost:51985

自定义端口：

```bash
PORT=8080 docker compose up -d
```

### Docker

```bash
docker build -t gaokao-query-all .
docker run -d -p 51985:51985 --name gaokao-query-all gaokao-query-all
```

### 本地运行

```bash
pip install flask
python app.py
```

访问 http://localhost:51985

## 项目结构

```
.
├── app.py              # Flask 后端（提供 /api/data 接口，预缓存 JSON）
├── index.html          # 前端页面（调 /api/data 加载数据，前端筛选/排序/导出）
├── data.json           # 投档数据（本科+专科，含办学性质）
├── requirements.txt    # Python 依赖
├── Dockerfile          # Docker 构建文件（分层优化，大文件放最后）
├── docker-compose.yml  # Docker Compose 配置（支持 PORT 环境变量）
└── README.md           # 说明文档
```

## 技术栈

- **前端**：原生 HTML/CSS/JavaScript（无框架依赖，前端完成所有筛选/排序/导出）
- **后端**：Python + Flask（提供数据 API，JSON 预缓存避免重复序列化）
- **部署**：Docker / Docker Compose

## API

| 端点 | 说明 |
|------|------|
| `GET /` | 返回前端页面 |
| `GET /api/data` | 返回全量投档数据（JSON 预缓存） |
| `GET /health` | 健康检查，返回 `{"status":"ok","records":20392}` |

## 架构

```
浏览器 → index.html → fetch('/api/data') → app.py → 读取 data.json → 返回预缓存 JSON
                     ↓
              前端 JS 筛选/排序/分页/导出
```
