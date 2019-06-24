from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import Articles
#blog列表页
def blog_title(request):
    articles = Articles.objects.all()
    return render(request,"blog/titles.html",{"blogs":articles})
#首页
def index(request):
   # blogs = BlogArticles.objects.all()
    return render(request,"index.html",)
#blog详情页
def blog_article(request,article_id):
    blog = get_object_or_404(Articles,id=article_id)
    pub = blog.publish
    return render(request,"blog/content.html",{"blog":blog,"publish":pub})
