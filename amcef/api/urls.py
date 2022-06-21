from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('posts', views.CreateGetAPIView.as_view()),
    path('posts/<int:pk>', views.PutDeleteAPIView.as_view()),
]
