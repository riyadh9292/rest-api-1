from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Test api view"""

    def get(self,request,format=None):
        """Return a list of APIView features"""
        an_apiview =[
        'Uses HTTP methods as functions (get,post,put,patch,delete)',
        'is similar to a traditional django view',
        'gives u the most control over your application logic',
        'is mapped manually to urls',
        ]
        return Response({'message':'hello','an_apiview':an_apiview})
