### Simple-Mall
该项目是用来资源转卖的，例如你的网盘有很多资源，你会采取发卡网、商城、等等，还要额外配置易支付、当面付等很是繁琐。本项目使用vd免签作为支付接口。

![后台](/public/admin.png)

![商品](/public/goods.png)

![我的](/public/profile.png)

#### 部署

首先拉取文件到本地，在项目根目录下创建 `.env` 文件填入内容

```dotenv
DEBUG=False
# 自定义key值
SECRET_KEY='django-insecure-(-yz_tpq1vm%g_-146461*ub52olpp2wm#qxdg535$)'

# 域名
DOMAIN=example.com

DB_HOST=mall-db
# 数据库名
MYSQL_DATABASE=mall-app
# 数据库密码
MYSQL_ROOT_PASSWORD=123456789

# vd免签配置
V_API_URL=https://example.com/
V_KEY=key
# 域名修改自己的
NOTIFY_URL=https://example.com/orders/pay-back/
```

安装nginx后在 `/etc/nginx/conf.d/` 目录创建 `simple-mall.conf`

```nginx
server {
    listen 80;
    server_name _;
    # 静态文件（对应 Django collectstatic 的 STATIC_ROOT）
    location /static/ {
        alias /app/staticfiles/;
    }
    # 反代 Django/Gunicorn
    location / {
        proxy_pass http://mall-app:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

然后运行 `docker-compose up -d`