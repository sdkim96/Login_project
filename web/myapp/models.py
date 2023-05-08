# myapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models



class MyUser(AbstractUser):
    # 추가적인 필드를 여기에 추가하세요 (선택 사항)
    pass
