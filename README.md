# 井字棋AI后端
## 实现逻辑
后端接收前端提交的棋盘状态，
在人类的回合返回人类决策后的获胜状态，
在AI的回合返回AI的决策以及AI决策后的获胜状态。
实现上采用Django框架，
根据前端提交的数据实例化GameDecision对象，
返回带有以上数据的json响应。
## 环境配置
> django环境: pip install django\
> drf: pip install djangorestframework\
> 跨域: pip install django-cors-headers\
> 在settings.py中CORS_ALLOWED_ORIGINS处配置前端URL,解决跨域问题
## 运行
> python manage.py makemigrations\
> python manage.py migrate\
> python manage.py runserver

