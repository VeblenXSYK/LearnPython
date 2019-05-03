### 使用 uWSGI 和 Nginx 部署 Flask 项目

#### 1、安装 Flask 和 uwsgi

```
pip install uwsgi flask
```

#### 2、创建一个简单的 Flask 项目

	见myapp.py文件

#### 3、创建uwsgi配置文件

	见myapp.ini文件

#### 4、uWSGI直接对flask应用进行部署

修改myapp.ini文件如下所示：

```
http=0.0.0.0:6666
#socket=/home/veblen/Project/Flask+uWSGI+Nginx/myapp.sock
```

启动uWSGI服务器：

```
uwsgi --ini myapp.ini
```

然后通过浏览器访问[127.0.0.1:6666]()

#### 5、配置nginx反向代理

修改myapp.ini文件如下所示：

```
#http=0.0.0.0:6666
socket=/home/veblen/Project/Flask+uWSGI+Nginx/myapp.sock
```

启动uWSGI服务器：

```
uwsgi --ini myapp.ini
```

修改nginx的配置文件，vi /etc/nginx/sites-available/default

```
server {
    listen 6666;
    server_name server_domain_or_IP;

        access_log /tmp/access.log;
        error_log /tmp/error.log;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/veblen/Project/Flask+uWSGI+Nginx/myapp.sock;
    }
}
```

**注意：nginx的配置文件是/etc/nginx/nginx.conf，这个配置文件中又引用了/etc/nginx/conf.d/和/etc/nginx/sites-enabled/这两个文件夹的配置文件，通过include来实现。所以，无论是直接在nginx.conf或者在conf.d、sites-enabled中配置都是可以的。**

重启nginx服务器：

```
/etc/init.d/nginx reload
```

然后通过浏览器访问[127.0.0.1:6666]()

**注意：nginx的worker process默认用户为www-data，由于nginx需要与uWSGI通信，所以nginx要有myapp.sock文件的写入权限，所以不能将myapp.sock文件放入/root目录下，这样当浏览器访问[127.0.0.1:6666]()会出现权限不够的问题。**

