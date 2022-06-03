from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied


def authenticate_user(validated_data):
    """
    Parameters
    ----------
    validated_data that contains:
        - username
        - password

    Raises
    ------
    PermissionDenied
        If the user does not exist or is inactive
    """

    user = authenticate(
        username=validated_data['username'], password=validated_data['password'])
    if user is None or not user.is_active:
        raise PermissionDenied('Invalid credentials')
    return user
