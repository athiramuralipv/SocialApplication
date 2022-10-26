from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import users,blogs
# Create your views here.

class BlogListView(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data=blogs)
    def post(self,request,*args,**kwargs):
        blog=request.data
        blog.append(blog)
class BlogDetailView(APIView):
    def get(self,request,*args,**kwargs):
        blog_id=kwargs.get("postId")
        blog=[post for post in blogs if post["postId"]==blog_id].pop()
        return Response(data=blog)

