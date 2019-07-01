from django.contrib import admin
from .models import ArticleColumn
# Register your models here.

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('column','created','user')
    list_filter = ("column",)


class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ('author','title','slug','column','body','updated')
    list_filter = ("column",)


admin.site.register(ArticleColumn,ArticleColumnAdmin)
