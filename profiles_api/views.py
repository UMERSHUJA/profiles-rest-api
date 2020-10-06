from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Return a list of APIView features """

        an_apiview = [
        'Uses http methods as function(get, post, update, put, patch, delete)',
        'its similiar to traditional django view',
        'give you the most control over your application logic',
        'Is mapped manually to urls',
        ]

        return Response(
            {
                'message': 'Hello!',
                'an_apiview': an_apiview
            }
        )

    def post(self, request):
        """ Create hello message with our name """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.error,
                status = status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """handling updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ handle a partial update of an object """
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
