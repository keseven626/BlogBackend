from  rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView
from .serializers import MyTokenObtainPairSerializer, UserProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .models import useraccount

user = settings.AUTH_USER_MODEL

# Create your views here.  
class MyTokenObtainPairView(TokenObtainPairView):
          serializer_class =  MyTokenObtainPairSerializer

@api_view(['GET'])
def UserProfile(request, pk):
    User = useraccount.objects.get(id=pk)
    serializer = UserProfileSerializer(User)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def FollowUser(request, pk):
    User = useraccount.objects.get(id=pk)
    obj = User.followers.add(request.data)
    serializer = UserProfileSerializer(obj)
    return Response(status=200)