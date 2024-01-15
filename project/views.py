from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.


def index(request):
    return render(request, 'project/index.html')


class Project_Post_View(APIView):

    serializer_class = Project_Post_Serializer

    def get(self, request):
        output = [{"title": output.title, "content": output.content}
                  for output in Project_Post.objects.all()]
        return Response(output)

    def post(self, request):

        serializer = Project_Post_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class Project_Category_View(APIView):

    serializer_class = Project_Category_Serializer

    def get(self, request):
        output = [{"name": output.name, "status": output.status}
                  for output in Category.objects.all()]
        return Response(output)

    def post(self, request):

        serializer = Project_Category_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class Project_Comment_View(APIView):

    serializer_class = Project_Comment_Serializer

    def get(self, request):
        output = [{"name": output.name, "message": output.message}
                  for output in Comment.objects.all()]
        return Response(output)

    def post(self, request):

        serializer = Project_Comment_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

