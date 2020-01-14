"""mysite URL Configuration

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
from django.urls import path, include

from blog.views import CommentsListView, MyRedirect, CreateComment, UpdateComment, DeleteComment, DetailComment

urlpatterns = [
    path('', CommentsListView.as_view(), name='index'),
    path('create_comment/', CreateComment.as_view(), name='create_comment'),
    path('update_comment/<int:pk>/', UpdateComment.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>/', DeleteComment.as_view(), name='delete_comment'),
    path('detail_comment/<int:pk>/', DetailComment.as_view(), name='detail_comment'),
    path('redirect/', MyRedirect.as_view(), name='redirect'),
    path('admin/', admin.site.urls)
]
