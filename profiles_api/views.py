from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View """
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
