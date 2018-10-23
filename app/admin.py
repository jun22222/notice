from django.contrib import admin
from .models import Notice


admin.site.register(Notice)
# Register your models here.

# 관리자 사이트 등록
#관리자로 접속할 수 있는 아이디를 만들자(터미널   python manage.py createsuperuser )