# DjangoBlog个人展示站
## 主要功能：
演示的博客站点内容较少：
- 实现网站首页

- 实现文章列表

- 实现文章内容页

- 实现标签页面

- 实现搜索页面

- 文章支持富文本编辑器，支持代码高亮。

- 支持文章全文搜索。

- 侧边栏功能，最新文章，最多阅读，标签云等。

- 后期增加功能





## 安装运行配置
由于数据量较少,数据库就采用sqlite3，如果要采用mysql,可以进行如下配置：打开settings.py文件，找到DATABASES，然后把它修改成如下代码：

修改成mysql如下：
```sql
############修改成mysql如下：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',    #你的数据库名称
        'USER': 'root',   #你的数据库用户名
        'PASSWORD': '445813', #你的数据库密码
        'HOST': '', #你的数据库主机，留空默认为localhost
        'PORT': '3306', #你的数据库端口
    }}

#由于mysql默认引擎为MySQLdb，在__init__.py文件中添加下面代码
#在python3中须替换为pymysql,可在主配置文件（和项目同名的文件下，不是app配置文件）中增加如下代码
#import pymysql
#pymysql.install_as_MySQLdb()
#如果找不到pymysql板块，则通过pip install pymysql进行安装。
```

由于涉及的步骤较多，附上快速部署链接，请移步：https://www.jianshu.com/p/d2993dd31b1e
