from rest_framework import serializers
from .models import movie , ratings ,watched_List

class Ratings_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ratings
        fields = ('UserId', 'MovieID', 'rating', 'review')




class Watched_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = watched_List
        fields = ('UserId', 'MovieTitle')