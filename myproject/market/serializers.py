from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class MyModelSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['name', 'page_count', 'category', 'author', 'price', 'image', 'published']