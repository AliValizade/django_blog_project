from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts_list'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_details'),
    path('add/', views.PostCreateView.as_view(), name='add_post'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
