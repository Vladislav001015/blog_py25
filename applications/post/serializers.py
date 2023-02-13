from rest_framework import serializers
from applications.post.models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = '__all__'
        # fields = ('id', )
        # exclude = ('post',)


class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField()
    images = PostImageSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Post
        # fields = ('title',)
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     # print(instance)
    #     representation =  super().to_representation(instance)
    #     # print(representation)
    #     # representation['name'] = 'John'
    #     # representation['owner'] = instance.owner.email
    #     representation['owner'] = instance.owner.email
    #     return representation
    
    # def create(self, validated_data):
    #     validated_data['owner'] = self.context['request'].user # request.user
    #     # print(validated_data)
    #     return super().create(validated_data)