from django.urls import path
from . import views # 'dot' means current app directory(blog)

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.CreatePost, name='post-create'),
    path('post/<slug:slug>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
    path('policies/', views.policies, name='policies'),
    path('features/', views.features, name='features'),
]