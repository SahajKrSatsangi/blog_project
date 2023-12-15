from django.urls import path
from .views import BlogListCreateView, custom_logout_view,home, create_blog, register
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name='home'),
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('create-blog/', create_blog, name='create-blog'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('account/profile/', BlogListCreateView.as_view(), name='blogs'),
]
