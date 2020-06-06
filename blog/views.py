from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def index(request):
    # 对Article进行声明并实例化，然后生成对象allarticle
    allarticle = Article.objects.all()
    # 把查询到的对象，封装到上下文
    context = { 'allarticle' : allarticle,}

    # 把上下文传递到模板里
    return render(request, 'index.html', context)



