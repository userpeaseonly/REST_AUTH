from rest_framework import serializers
from .models import CustomUser as User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
