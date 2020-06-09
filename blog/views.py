from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Banner, Article, Tag


def index(request):
    # 对Article进行声明并实例化，然后生成对象allarticle
    allcategory = Category.objects.all()
    allarticle = Article.objects.all().order_by('-id')[0:10]
    banner = Banner.objects.filter(is_active=True)[0:4]  # 查询所有幻片灯图数据，并进行切片
    tui = Article.objects.filter(tui_id=1)[:3]  # 查询推荐位ID为1的文章
    hot = Article.objects.all().order_by('views')[:10]  # 通过浏览数进行排序
    remen = Article.objects.filter(tui_id=2)[:6]
    tags = Tag.objects.all()
    # 把查询到的对象，封装到上下文
    context = {
        'allcategory': allcategory,
        'allarticle': allarticle,
        'hot': hot,
        'remen': remen,
        'banner': banner,
        'tui': tui,
        'tags': tags
        }

    # 把上下文传递到模板里
    return render(request, 'default/index.html', context)


def list(request, lid):

    pass


def show(request, sid):
    pass


def tag(request, tag):
    pass


def search(request, search):
    pass


def about(request, about):
    pass


















