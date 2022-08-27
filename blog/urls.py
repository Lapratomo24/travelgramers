from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.CreatePost.as_view(), name='create'),
    path('update/<slug:slug>', views.UpdatePost.as_view(), name='update'),
    path('delete/<slug:slug>', views.PostDeletion.as_view(), name='delete'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
