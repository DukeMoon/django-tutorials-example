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


### DataBase Settings & Django Model & Migration & Django Admin
编写更多视图
#### HttpResponse
``` python
from django.http import HttpRespoget_querysetnse

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
```
#### render
``` python
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```
#### 去除模板中的硬编码 URL
``` html
> polls/index.html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```
#### 为 URL 名称添加命名空间
``` python
> polls/urls.py
app_name = 'polls'
> polls/index.html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

### make and upload pip package
mysite/polls全部移入django-polls文件夹准备打包用

1. 创建README.rst（现在也支持.md）文件，进行项目及使用说明
2. 创建LICENSE文件，进行开源协议说明
3. 创建setup.py文件，进行包属性配置
4. 创建MANIFEST.in文件，进行打包流程管理
5. $ python setup.py sdist ;生成package
6. $ python -m pip install --upgrade twine ; 安装twine准备上传
7. 注册一个[https://test.pypi.org][test.pypi]账号准备上传用（这是pip专用测试环境，区分于平时正常用的[https://pypi.org][pypi]，账号也不互通。）
8. $ twine upload --repository-url https://test.pypi.org/legacy/ dist/* ; 上传到测试
9. $ pip install --index-url https://test.pypi.org/simple/ django-tutorials-polls ; 从测试pip安装django-tutorials-polls包




[test.pypi]: https://test.pypi.org
[pypi]: https://pypi.org

