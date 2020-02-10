from pprint import pprint

from rest_framework.authentication import get_authorization_header
from rest_framework.permissions import BasePermission


class CustomPerm(BasePermission):
    def has_permission(self, request, view):
        query_string = request.META.get('QUERY_STRING')
        print(query_string)
        if not query_string:
            return False
        key, value = query_string.split('=')
        if key == 'api_key' and value != '1234':
            return True
        return False