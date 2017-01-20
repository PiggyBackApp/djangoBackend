from posts.models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description', 'timePosted', 'postType', 'origin', 'destination', 'emptySeats', 'passengerCapacity', 'status')