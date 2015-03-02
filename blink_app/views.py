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
    search_fields = ('title','director__name','characters__actor__name')

class ContentViewSet(viewsets.ModelViewSet):

    serializer_class = ContentSerializer
    queryset = Content.objects.filter()

class YearSearchViewSet(generics.ListAPIView):

    queryset = Content.objects.all().order_by('title')
    serializer_class = YearSearchSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('release_year',)

class GenreSearchViewSet(generics.ListAPIView):

    queryset = Content.objects.all().order_by('title')
    serializer_class = GenreSearchSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('genre__name',)

# class SearchTest(generics.ListAPIView):
#
#     queryset = Content.objects.filter(contains="Bat")
#     serializer_class = SearchSerializer

