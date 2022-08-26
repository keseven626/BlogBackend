from django.urls import path
from .views import CreatePost, Posts, PostDetail, PostDelete, PostUpdate, UserProfile, CategoryPost, PostComment

urlpatterns = [
          path('CreatePost/',CreatePost, name='create-post' ),
          path('Posts/', Posts.as_view(), name='posts' ),
          path('category/<str:category>/',CategoryPost, name='post-category' ),
          path('post/<str:pk>/', PostDetail, name='post-detail' ),
          path('search/<str:searchPost>/',Posts.as_view(), name='post' ),
          path('update-post/<str:pk>/',PostUpdate.as_view(), name='update-post' ),
          path('comment/<str:pk>/',PostComment, name='PostComment' ),
          path('delete-post/<str:pk>/',PostDelete, name='post-delete' ),
          path('User/<str:pk>/',UserProfile, name='user-profile' ),
]
