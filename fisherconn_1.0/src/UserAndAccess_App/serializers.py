from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups','password')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('productid', 'productname', 'productprice', 'productdesc')