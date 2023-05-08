from django.contrib import admin


# http://127.0.0.1:8000/admin/ 에서 접속함
# id : super, password : qwerty
# 김성동 계정 : id:rlatjdehd, pwd : 590223!apq
# Register your models here.
from django.contrib import admin
from .models import MyUser

admin.site.register(MyUser)
