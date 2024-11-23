from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from django.conf import settings

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Utility to set the refresh token in a secure HttpOnly cookie
def set_refresh_token_cookie(response, refresh_token):
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,  # Prevent JavaScript access
        secure=True,  # Only over HTTPS in production
        samesite="Strict",  # CSRF protection
        max_age=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds(),
    )


# Login View: Issues both access and refresh tokens
class LoginView(APIView):
    def post(self, request):
        from django.contrib.auth import authenticate

        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            response = Response({"access_token": str(refresh.access_token)}, status=status.HTTP_200_OK)
            set_refresh_token_cookie(response, str(refresh))  # Set refresh token in a cookie
            return response
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# Token Refresh View: Generates a new access token using the refresh token from cookies
class TokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")
        if not refresh_token:
            return Response({"detail": "Refresh token not found"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            new_access_token = refresh.access_token
            # Optionally rotate refresh tokens (enabled by SIMPLE_JWT settings)
            response = Response({"access_token": str(new_access_token)}, status=status.HTTP_200_OK)
            set_refresh_token_cookie(response, str(refresh))
            return response
        except TokenError as e:
            return Response({"detail": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)


# Logout View: Blacklists the refresh token and removes the cookie
class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")
        if not refresh_token:
            return Response({"detail": "Refresh token not found"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            refresh.blacklist()  # Blacklist the token
            response = Response({"detail": "Logged out successfully"}, status=status.HTTP_200_OK)
            response.delete_cookie("refresh_token")  # Remove the refresh token cookie
            return response
        except TokenError:
            return Response({"detail": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)
