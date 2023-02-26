from rest_framework import serializers
from django.contrib.auth.models import User


# class RegisterSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'password')
        
#     def validate(self,data):
#         if User.objects.filter(username=data["username"]).exists():
#             raise serializers.ValidationError("Username already exists")
#         return data
    
#     def create(self,validated_data):
#         user = User.objects.create(
#             username=validated_data['username'].lower(),
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#         )
#         user.set_password(validated_data['password'])


#         return validated_data


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


