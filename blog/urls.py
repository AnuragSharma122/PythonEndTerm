from django.contrib import admin
from django.urls import path
from . import views
from .views import PostDetailView,PostUpdateView,PostDeleteView,likePostApp,addComment



urlpatterns = [
    path('', views.home, name='post-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('likepost/<pk>', views.likePostApp, name='LikePost'),
    path('about/',views.about, name='post-about'),
    path('post/<int:pk>/',views.addComment)
]
