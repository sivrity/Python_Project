from rest_framework import serializers
from . models import *


class Project_Post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Post
        fields = '__all__'


class Project_Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Project_Comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'