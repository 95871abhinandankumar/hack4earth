from django.urls import path
from . import views
from .views import PostCreateView, PostListView, PostDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('posts/', PostListView.as_view(), name='blog-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
    path('', views.home, name='blog-home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
