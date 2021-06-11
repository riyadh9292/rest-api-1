from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.authentication import TokenAuthentication
from . import Permissions

from . import serializers
from . import models



class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of APIView features"""
        an_apiview =[
        'Uses HTTP methods as functions (get,post,put,patch,delete)',
        'is similar to a traditional django view',
        'gives u the most control over your application logic',
        'is mapped manually to urls',
        ]
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({"method":"PUT"})

    def patch(self,request,pk=None):
        """handle a partial update an object"""
        return Response({"method":"PATCH"})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({"method":"delete"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (Permissions.UpdateOwnProfile,)
