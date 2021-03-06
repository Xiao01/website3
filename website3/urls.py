"""website3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views import static ##新增
from django.conf import settings ##新增
from django.conf.urls import url ##新增


from django.urls import path, re_path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('home/',TemplateView.as_view(template_name='home.html'),name='home'),
    path('', include('blog.urls',namespace='blog')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls',namespace='blog')),
    path('account/', include('account.urls',namespace='account')),
    path('article/',include('article.urls',namespace='article')),
    path('image/',include('image.urls',namespace='image')),
    path('course/',include('course.urls',namespace='course')),

    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),



];


from django.conf.urls.static import static as staic1
urlpatterns += staic1(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

