# django-tutorials-example
Django2.0.8 tutorials example

## 缘起
> 接触Django一段时间，却一直没有实践过Tutorial教程。
> 特地结合接触过的业务进行查漏补缺。

### Create A New Django Project and APP
安装Django依赖

    $ pip install Django==2.0.8
创建一个Django项目
    
    $ django-admin startproject mysite
运行测试服务器

    $ python manage.py runserver
创建一个APP

    $ python manage.py startapp polls



### DataBase Settings & Django Model & Migration & Django Admin
配置数据库
``` python
# mysite/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

创建模型
``` python
# polls/models.py

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
```

激活模型
``` python
# mysite/settings.py

INSTALLED_APPS += [
    "polls"
]
```

迁移模型并应用到数据库
    
    $ python manage.py makemigrations polls  # 迁移模型，生成migrations文件
    $ python manage.py sqlmigrate polls 0001  # 查看migrations文件对应的sql语句
    $ python manage.py migrate  # 应用到数据库
  
在交互式命令行中运行Django
    
    $ python manage.py shell

创建管理员账号

    $ python manage.py createsuperuser

配置Django Admin
``` python
# polls/admin.py

admin.site.register(Question)
```