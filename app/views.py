from django.shortcuts import render
from .models import Notice



def index(request):
    notice = Notice.objects.all()


    return render(request, 'app/index.html', {'list' : notice})     # 잘 되는지 확인하기 위해 HttpResponse()하는거 보통은 render()
# Create your views here.

                 # kk 여기로 넘어옴
def detail(request, num):         #프라이머리키
    # item = Notice.objects.get(pk = 1)
    item = Notice.objects.get(id = num)
    return  render(request, 'app/detail.html', {'item' : item})