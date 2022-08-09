from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id','name','content','created_at','updated_at')


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'