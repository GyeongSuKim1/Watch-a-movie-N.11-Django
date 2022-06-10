from django.contrib import admin
# 생성한 model을 가져옴
from .models import UserModel

# Register your models here.

admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다