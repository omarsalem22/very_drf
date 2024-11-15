from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Initialize the serializer with the request data
        serializer = RegisterUserSerializer(data=request.data)

        # Check if the provided data is valid
        if serializer.is_valid():
            # Save the new user and return a success response
            user = serializer.save()
            return Response({"detail": "Registration successful!"}, status=status.HTTP_201_CREATED)
        else:
            # Return validation errors if any
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlackListToken(APIView):
    permission_classes=[AllowAny]
    
    def post(self,request):
        
        try:
            refresh_token=request.data['refresh_token']
            token=RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        
