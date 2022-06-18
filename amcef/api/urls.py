from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('posts', views.PostAPIView.as_view()),
    path('posts/edit/<int:pk>', views.PostAPIView.as_view()),
    path('delete', views.deletePost),
]