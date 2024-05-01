from .models import *
from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer



class ProducSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name', 'price']


class ProducDetailedSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'price', 'page_count', 'category', 'author', 'stock']



