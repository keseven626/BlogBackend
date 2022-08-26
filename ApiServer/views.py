
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.generics import  ListAPIView, UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination
from .serializers import PostModelSerializer, PostCreateSerializer, CommentSerializer
from .models import  Post, Category, Comment


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def CreatePost(request):
    serializer = PostCreateSerializer(data=request.data)
    if serializer.is_valid() :    
        serializer.save()
    return Response(serializer.data, status=201)

class Posts(ListAPIView):
    queryset = Post.objects.all().filter(publish='publish')
    serializer_class = PostModelSerializer
    pagination_class = PageNumberPagination
    

    def get_queryset(self):
      qs = super().get_queryset().filter(publish='publish')
      if 'searchPost' in self.kwargs:
          search = self.kwargs['searchPost']
          if search:
            qs = Post.objects.all().filter(title__icontains=search)
      return  qs

@api_view(['GET', 'POST',])
def PostComment(request, pk):
    if request.method == 'GET':
        comment = Comment.objects.all().filter(post_comment=pk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status=200)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=200)
        
@api_view(['GET', 'POST',])
def PostDetail(request, pk):
            post = Post.objects.get(id=pk)
            serializer = PostModelSerializer(post, many=False)

            if request.method == 'POST':
                if 'like' in request.data:
                    obj = post.like.add(request.data['user'])
                    serializer = PostModelSerializer(obj)
                    return Response(status=200)

                if 'Unlike' in request.data:
                    obj = post.like.remove(request.data['user'])
                    serializer = PostModelSerializer(obj)
                    return Response(status=200)
            return Response(serializer.data, status=200)

class PostUpdate(UpdateAPIView):
             queryset = Post.objects.all()
             serializer_class = PostCreateSerializer
             lookup_field = 'pk'

             def update(self, request,  **kwargs):
                instance = self.queryset
                serializer = self.get_serializer(instance, request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'post saved'})
                else:
                    return Response({'message': 'post not saved'})
                    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def PostDelete(request, pk):
            post = Post.objects.get(id=pk)
            post.delete()
            return Response(status=200)

def UserProfile(request, pk):
    post = Post.objects.all().filter(id=pk) 
    context={
        post: post
        } 
    return JsonResponse(context, status=200) 

@api_view(['GET',])
def CategoryPost(request, category):
    post = Post.objects.filter(category__name__iexact=category)
    serializer = PostModelSerializer(post, many=True)
    return Response(serializer.data, status=200)
                                                                                                                                                                                                    