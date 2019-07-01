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
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "account"

urlpatterns = [
    #path('login/',views.user_login2,name='user_login'),
    path('login/',auth_views.LoginView.as_view(template_name='account/login2.html'),name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
    path('register/',views.register,name='user_register'),
    path('password-change/',
         auth_views.PasswordChangeView.as_view(
             template_name = "account/password_change_form.html",
             success_url ="/account/password-change-done/"), name ='password_change'),
    path('password-change-done/',auth_views.PasswordChangeDoneView.as_view(
        template_name="account/password_change_done.html"),name='password_change_done'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(
        template_name = 'account/password_reset_done.html'),
    name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name = "account/password_reset_confirm.html",
             success_url = "/account/password-reset-complete/"),
         name = "password_reset_confirm"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name = 'account/password_reset_complete.html'),
         name = 'password_reset_complete'),
    path('password-reset/',auth_views.PasswordResetView.as_view(
        template_name = "account/password_reset_form.html",
        email_template_name = "account/password_reset_email.html",
        subject_template_name = "registration/password_reset_subject.txt",
        success_url = "/account/password-reset-done/"),
    name = 'password_reset'),
    path('my-information/',views.myself,name='my_information'),
    path('edit-my-information/',views.myself_edit,name="edit_my_information"),
    path('my-image/',views.my_image,name="my_image"),
]


