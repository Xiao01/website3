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
from django.views.generic import TemplateView

from course.views import AboutView, CourseListView, ManageCourseListView, CreateCourseView, DeleteCourseView, \
    CreateLessonView, ListLessonsView, DetailLessonView, StudentListLessonView

app_name = "course"
urlpatterns = [
    path('about/',AboutView.as_view(),name="about"),
    path('course-list/',CourseListView.as_view(),name="course_list"),
    path('manage-course/',ManageCourseListView.as_view(),name="manage_course"),
    path('create-course/',CreateCourseView.as_view(),name="create_course"),
    path('delete-course/<int:pk>',DeleteCourseView.as_view(),name="delete_course"),
    path('create-lesson/',CreateLessonView.as_view(),name="create_lesson"),
    path('list-lessons/<int:course_id>/',ListLessonsView.as_view(),name="list_lessons"),
    path('detail-lessons/<int:lesson_id>/',DetailLessonView.as_view(),name="detail_lesson"),
    path('lessons-list/<int:course_id>/',StudentListLessonView.as_view(),name="lessons_list"),



];

