from rest_framework import serializers
from .models import NewUser

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}  # Ensuring password is not exposed in response
    
    def create(self, validated_data):
        # Pop the password and hash it before saving the user
        password = validated_data.pop('password')
        
        # Create the user instance
        instance = self.Meta.model(**validated_data)
        
        if password:
            # Hash the password and save the instance
            instance.set_password(password)
            instance.save()
            return instance
        
        raise serializers.ValidationError("Password is required")
