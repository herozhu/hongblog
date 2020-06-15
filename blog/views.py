from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Banner, Article, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    # 对Article进行声明并实例化，然后生成对象allarticle
    allarticle = Article.objects.all().order_by('-id')[0:10]  # 倒序查询出10条文章
    banner = Banner.objects.filter(is_active=True)[0:4]  # 查询所有幻片灯图数据，并进行切片，显示4章图片
    tui = Article.objects.filter(tui_id=1)[:3]  # 查询推荐位ID为1的文章
    hot = Article.objects.all().order_by('views')[:10]  # 通过浏览数进行排序
    tags = Tag.objects.all()  # 查询所有的标签
    link = Link.objects.all()  # 查询所有的友情链接

    #  locals()的作用是返回一个包含当前作用域里面的所有变量和它们的值的字典,优化了context = {...}的方式。
    return render(request, 'default/index.html', locals())


def list(request, lid):
    list = Article.objects.filter(category_id=lid)  # 获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=lid)  # 获取当前文章的栏目名
    #  分页器的实现
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
            list = paginator.page(page)
    except PageNotAnInteger:
           list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
           list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    #  locals()的作用是返回一个包含当前作用域里面的所有变量和它们的值的字典,优化了context = {...}的方式。
    return render(request, 'default/list.html', locals())


def show(request, sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    allcategory = Category.objects.all()  # 获取导航上的所有分类
    hot = Article.objects.all().order_by('?')[:10]  # 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    next_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'default/show.html', locals())


def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)  # 通过文章标签进行查询文章
    tname = Tag.objects.get(name=tag)  # 获取当前搜索的标签名
    page = request.GET.get('page')
    paginator = Paginator(list, 10)  # 对查询到的数据对象list进行分页，设置超过10条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'default/tags.html', locals())


def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss)  # 获取到搜索关键词通过标题进行匹配
    page = request.GET.get('page')
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'default/search.html', locals())


def about(request):
    return render(request, 'default/page.html', locals())


def global_variable(request):
    allcategory = Category.objects.all()  # 查询出所有栏目分类
    remen = Article.objects.filter(tui_id=2)[:6]  # 通过后台推荐位ID=2的热门推荐，显示6条相关的文章
    tags = Tag.objects.all()  # 获取右侧上的所有标签
    return locals()

















