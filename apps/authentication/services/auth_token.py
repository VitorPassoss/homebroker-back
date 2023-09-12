from datetime import datetime, timedelta

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken


class CustomTokenObtainPairView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # Generate an access token with a 7-day expiration
            access_token = AccessToken()
            access_token["user_id"] = user.id
            access_token["exp"] = datetime.utcnow() + timedelta(days=7)

            access_token_str = str(access_token)

            return Response(
                {
                    "access_token": access_token_str,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
