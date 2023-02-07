from rest_framework import serializers
from django.contrib.auth import get_user_model
from applications.account.send_email import send_activation_code

User = get_user_model()  # CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        required=True,
        min_length=6,
        write_only=True 
    )

    class Meta:
        # model = CustomUser
        model = User
        fields = ('email', 'password', 'password2')
    

    def validate_email(self, email):
        print('Hello')
        return email
    
    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Password did not match!!!')

        return attrs
    

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)
        return user