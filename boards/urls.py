from django.urls import path
from . import views

urlpatterns= [
    path('', views.postlist),
    path('<int:post_num>/', views.postpage),
]