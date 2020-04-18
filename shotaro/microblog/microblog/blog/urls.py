from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from blog.views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('',BlogListView.as_view(), name='index'),
    path('detail/<int:pk>/',BlogDetailView.as_view(), name='blog_detail'),
    path('create/',BlogCreateView.as_view(),name='blog_create'),
    path('update/<int:pk>/',BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/',BlogDeleteView.as_view(), name='blog_delete'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
]
