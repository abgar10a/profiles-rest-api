from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URL\'s',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with ur name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating request(firstname lastname)-update"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
        else:
            message = 'None'
        return Response({'method': 'PUT', 'message':message})

    def patch(self,request,pk=None):
        """Hnadle partial update of object(firstname lastname)-update first name"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""

        return Response({'method':'DELETE'})



class HellowViewSet(viewsets.ViewSet):
    """Test api viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""
        a_viewset = [
        'Uses actions(list, create,retreive,update,partial_update)',
        'automatically maps to urls using routers',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """get obj by id"""
        return Response({'http-method':'get'})

    def update(self,request,pk=None):
        return Response({'http-method':'get'})

    def partial_update(self,request,pk=None):
        return Response({'http-method':'patch'})

    def destroy(self,request,pk=None):
        return Response({'http-method':'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """create and update profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


