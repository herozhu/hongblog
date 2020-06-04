from django.contrib import admin
from .models import Category, Tag, Tui, Article, Banner, Link
# 导入需要管理的数据库表


admin.site.site_header = '坤宏集团AI表格系统'
admin.site.site_title = '坤宏集团管理系统'


# 注册文章分类模型
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


# 注册标签模型
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# 注册推荐位模型
@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# 注册文章模型
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表里显示想要显示的字段
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time')
    # 满50条数据就自动分页
    list_per_page = 50
    # 后台数据列表排序方式
    # ordering = ('created_time',)
    # 设置点击标题或者ID进行编辑
    list_display_links = ('id', 'title')


# 注册背景图模型
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


# 注册友情链接模型
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link_url')
















