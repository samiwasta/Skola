from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.BASE, name='base'),
    path('', views.HOME, name='home'),
    path('course', views.COURSE, name='course'),
    path('course/html', views.HTML, name= 'course_html')
]
