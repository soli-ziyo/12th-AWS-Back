from django.shortcuts import render
from rest_framework import views
from .models import Blog
from .serializers import *
from rest_framework.response import Response
from rest_framework.status import *


# Create your views here.


class BlogDetailView(views.APIView):
    def get(self, request):
        blogs=Blog.objects.all()
        serializers=BlogSerializer(blogs,many=True)
        return Response({'message':'화이팅~!','data': serializers.data}, status=HTTP_200_OK)
    