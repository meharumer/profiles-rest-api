from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of API View features"""
        an_apiview = [
        'Uses HTTP methods as get post put delete',
        'Is similiar to traditional Django views',
        'gives you more control over logic',
        'is mapped manually to URLs',
        ]
        return Response({
        'message':'hello',
        'an_apiview':an_apiview
        })
