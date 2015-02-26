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
    search_fields = ('title', 'release_year', 'director__name','characters__name', 'characters_actor_name')


class ContentViewSet(viewsets.ModelViewSet):

    serializer_class = ContentSerializer
    queryset = Content.objects.filter()


# class ActorViewSet(viewsets.ModelViewSet):
#
#     read_only=True
#     queryset = Content.objects.filter(title__startswith='B')
#     serializer_class = SearchSerializer
#
# class GenreViewSet(viewsets.ModelViewSet):
#
#     read_only=True
#     queryset = Content.objects.filter(title__startswith='B')
#     serializer_class = SearchSerializer