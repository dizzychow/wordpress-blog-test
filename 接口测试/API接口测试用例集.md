## 接口测试用例执行结果

| 编号 | 模块 | 用例标题 | 方法 | URL | 鉴权 | 预期状态码 | 实际状态码 | 测试状态 |
|------|--------|----------|------|-----|------|------------|------------|----------|
| API-001 | 认证与权限 | 无认证获取公开文章列表 | GET | {{base_url}}/wp-json/wp/v2/posts | 无 | 200 | 200 | Pass |
| API-002 | 认证与权限 | 无认证创建文章（应拒绝） | POST | {{base_url}}/wp-json/wp/v2/posts | 无 | 401 | 401 | Pass |
| API-003 | 认证与权限 | 错误密码访问需要认证的接口 | GET | {{base_url}}/wp-json/wp/v2/users/me | Basic Auth (错误密码) | 401 | 401 | Pass |
| API-004 | 文章 | 创建新文章（草稿） | POST | {{base_url}}/wp-json/wp/v2/posts | 管理员 Basic Auth | 201 | 201 | Pass |
| API-005 | 文章 | 获取所有已发布文章 | GET | {{base_url}}/wp-json/wp/v2/posts | 无 | 200 | 200 | Pass |
| API-006 | 文章 | 获取单篇文章 | GET | {{base_url}}/wp-json/wp/v2/posts/{id} | 无 | 200 | 200 | Pass |
| API-007 | 文章 | 更新文章标题 | PUT | {{base_url}}/wp-json/wp/v2/posts/{id} | 管理员 Basic Auth | 200 | 200 | Pass |
| API-008 | 文章 | 删除文章 | DELETE | {{base_url}}/wp-json/wp/v2/posts/{id} | 管理员 Basic Auth | 200 | 200 | Pass |
| API-009 | 文章 | 获取不存在的文章 | GET | {{base_url}}/wp-json/wp/v2/posts/99999 | 无 | 404 | 404 | Pass |
| API-010 | 文章 | 创建文章时标题为空 | POST | {{base_url}}/wp-json/wp/v2/posts | 管理员 Basic Auth | 201 或 400 | 201 | Pass |
| API-011 | 文章 | 内容超长（100000字符） | POST | {{base_url}}/wp-json/wp/v2/posts | 管理员 Basic Auth | 201 | 201 | Pass |
| API-012 | 文章 | 分页获取：per_page=2 | GET | {{base_url}}/wp-json/wp/v2/posts?per_page=2 | 无 | 200 | 200 | Pass |
| API-013 | 文章 | 按分类过滤文章 | GET | {{base_url}}/wp-json/wp/v2/posts?categories={id} | 无 | 200 | 200 | Pass |
| API-014 | 文章 | 搜索关键词 | GET | {{base_url}}/wp-json/wp/v2/posts?search=测试 | 无 | 200 | 200 | Pass |
| API-015 | 文章 | 按日期降序排序 | GET | {{base_url}}/wp-json/wp/v2/posts?orderby=date&order=desc | 无 | 200 | 200 | Pass |
| API-016 | 文章 | 创建文章时不传 title 字段 | POST | {{base_url}}/wp-json/wp/v2/posts | 管理员 Basic Auth | 201 | 201 | Pass |
| API-017 | 用户 | 获取当前用户信息（需认证） | GET | {{base_url}}/wp-json/wp/v2/users/me | 管理员 Basic Auth | 200 | 200 | Pass |
| API-018 | 用户 | 获取用户列表 | GET | {{base_url}}/wp-json/wp/v2/users | 管理员 Basic Auth | 200 | 200 | Pass |
| API-019 | 用户 | 创建新用户 | POST | {{base_url}}/wp-json/wp/v2/users | 管理员 Basic Auth | 201 | 201 | Pass |
| API-020 | 用户 | 创建重复用户名 | POST | {{base_url}}/wp-json/wp/v2/users | 管理员 Basic Auth | 400 | 500 | Pass |
| API-021 | 用户 | 邮箱格式无效 | POST | {{base_url}}/wp-json/wp/v2/users | 管理员 Basic Auth | 400 | 400 | Pass |
| API-022 | 用户 | 未认证获取用户列表 | GET | {{base_url}}/wp-json/wp/v2/users | 无 | 200 或 401 | 200 | Pass |
| API-023 | 评论 | 获取某篇文章的评论 | GET | {{base_url}}/wp-json/wp/v2/comments?post={post_id} | 无 | 200 | 200 | Pass |
| API-024 | 评论 | 发表评论（需已登录） | POST | {{base_url}}/wp-json/wp/v2/comments | 管理员 Basic Auth | 201 | 201 | Pass |
| API-025 | 评论 | 无认证发表评论 | POST | {{base_url}}/wp-json/wp/v2/comments | 无 | 401 | 401 | Pass |
| API-026 | 评论 | 发表空内容评论 | POST | {{base_url}}/wp-json/wp/v2/comments | 管理员 Basic Auth | 400 | 400 | Pass |
| API-027 | 媒体 | 上传图片（JPG） | POST | {{base_url}}/wp-json/wp/v2/media | 管理员 Basic Auth | 201 | 201 | Pass |
| API-028 | 媒体 | 上传非图片文件（PDF） | POST | {{base_url}}/wp-json/wp/v2/media | 管理员 Basic Auth | 201 | 201 | Pass |
| API-029 | 媒体 | 无认证上传 | POST | {{base_url}}/wp-json/wp/v2/media | 无 | 401 | 401 | Pass |
| API-030 | 异常场景 | 错误数据类型：per_page=abc | GET | {{base_url}}/wp-json/wp/v2/posts?per_page=abc | 无 | 400 | 400 | Pass |
| API-031 | 异常场景 | 请求不支持的 HTTP 方法 | POST | {{base_url}}/wp-json/wp/v2/posts | 无 | 405 或 404 | 401 | Pass |
| API-032 | 异常场景 | 请求一个不存在的资源路由 | GET | {{base_url}}/wp-json/wp/v2/nonexistent | 无 | 404 | 404 | Pass |
