from django.contrib.auth.models import User
from models import Content,Character,Person,PersonType
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email')

class SearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ('title','release_year','poster','id')

class PersonTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonType
        fields = ('name',)

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id','name','headshot','imdb_url')

class WriterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id','name','headshot','imdb_url')

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id','name','headshot','imdb_url')

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    actor = ActorSerializer(many=True, read_only=True)
    class Meta:
        model = Character
        fields = ('id','name','imdb_url','actor')

class ContentSerializer(serializers.HyperlinkedModelSerializer):
    director = DirectorSerializer(many=True, read_only=True)
    writer = WriterSerializer(many=True, read_only=True)
    characters = CharacterSerializer(many=True, read_only=True)
    class Meta:
        model = Content
        fields = ('id','title','release_date','release_year','runtime','mpaa_rating','imdb_rating','imdb_url','poster','synopsis','netflix_url','hulu_url','prime_url','director','writer','characters','budget','revenue',)