### Default-Template-Django
使用了Django默认后台（采用simpleui）+ Drf + Jwt。
Django版本:5.2
项目结构已经基本完善，拉取到本地并在项目根目录创建 `.env` 按下面格式开箱即用（SECRET_KEY自行更改）。

```dotenv
DEBUG=True
SECRET_KEY='django-insecure-(-yz_tpq1vm%g_-146461*ub52olpp2wm#qxdg535$)'


# 部署时候用到的mysql，开发阶段不需要设置
#MYSQL_DATABASE=app
#MYSQL_ROOT_PASSWORD=123456
```

基本开发配置已经完善，拥有以下配置:
1. 统一了Drf的错误处理
2. 响应格式（确切地说是json类型的响应包含Django的JsonResponse进行了返回格式自定义）
3. simplejwt 登录时的响应内容进行了统一化（自定义载荷和响应内容）
4. 日志采用loguru，在 `settings.py` 导出使用。
5. 项目部署采用gunicorn 且内置了Dockerfile和docker-compose.yaml 方便部署。