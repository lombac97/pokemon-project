from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from auth_service.services import authenticate_user


class LoginView(APIView):
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()

    def post(self, request: Request):
        try:
            input = self.InputSerializer(data=request.data)
            input.is_valid(raise_exception=True)
            user = authenticate_user(
                input.validated_data)
            token = Token.objects.get_or_create(user=user)
            return Response({"token": str(token[0])})
        except Exception as error:
            raise error
