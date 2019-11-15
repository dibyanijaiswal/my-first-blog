from django.urls import path
from . import views

urlpatterns = [
    path('',views.postlist,name='postlist'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
]