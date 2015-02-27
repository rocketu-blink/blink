from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import generics
from blink_app.serializers import *


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class SearchViewSet(generics.ListAPIView):

    queryset = Content.objects.all()
    serializer_class = SearchSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'director__name', 'characters__actor__name')

class ContentViewSet(viewsets.ModelViewSet):

    serializer_class = ContentSerializer
    queryset = Content.objects.filter()