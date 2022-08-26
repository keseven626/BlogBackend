from zipfile import Path
from       django.urls import        path
from  rest_framework_simplejwt.views import   TokenRefreshView
from .views import   MyTokenObtainPairView, UserProfile, FollowUser

urlpatterns=[
            path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
            path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
            path('user/<int:pk>/', UserProfile , name='user-profile' ),
            path('user/follow/<int:pk>/', FollowUser , name='follow-user' )
          ]
