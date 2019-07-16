from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Pokemon, Areas

class PokemonType(DjangoObjectType):

    class Meta:
        model = Pokemon
        interfaces = (graphene.relay.Node,)

class AreaType(DjangoObjectType):

    class Meta:
        model = Areas
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):

    all_pokemon = graphene.List(PokemonType)
    pokemon = graphene.Field(pokemonType, id=graphene.Int())
    all_areas = graphene.List(AreaType)
    area = graphene.Field(areaType, id=graphene.Int())

    def resolve_all_pokemon(self, info):
        return Pokemon.objects.all()

    def resolve_pokemon(self, info, **kwargs):
        id = kwargs.get('id')
        return Pokemon.objects.get(pk=id)

    def resolve_all_areas(self, info):
        return Areas.objects.all()

    def resolve_area(self, info, **kwargs):
        id = kwargs.get('id')
        return Areas.objects.get(pk=id)

schema = graphene.Schema(query=Query)
