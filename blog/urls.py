from django.urls import path
from . import views

urlpatterns = [
    path('',views.postlist,name='postlist'),
    path('post/<int:pk>/',views.postdetail,name='postdetail'),
    path('post/new/',views.postnew,name='postnew'),
    path('post/<int:pk>/edit/',views.postedit,name='postedit'),
]