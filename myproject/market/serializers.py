from .models import *
from rest_framework.serializers import ModelSerializer



class ProducSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name', 'price']


class ProducDetailedSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'price', 'page_count', 'category', 'author', 'stock']


class BookUpdateSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['stock']




