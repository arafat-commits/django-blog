from django. urls import path
from . import views # 'dot' means current directory.(blog)
from .views import (
	PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView
)

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.CreatePost, name='post-create'),
    path('post/<slug:slug>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
    path('policies/', views.policies, name='policies'),
    path('features/', views.features, name='features'),
    path('contact/', views.contact, name='contact'),
]