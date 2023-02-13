from rest_framework import serializers
from applications.post.models import Post, PostImage, Comment


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

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)

        request = self.context.get('request')
        data = request.FILES
        # for i in data.getlist('images'):
        #     PostImage.objects.create(post=post,image=i)
        image_objects = []
        for i in data.getlist('images'):
            image_objects.append(PostImage(post=post,image=i))
        PostImage.objects.bulk_create(image_objects)

        return post


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'