from rest_framework import serializers
from applications.feedback.models import Like

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'