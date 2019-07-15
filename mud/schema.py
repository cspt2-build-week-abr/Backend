from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Pokemon

class PokemonType(DjangoObjectType):

    class Meta:
        model = Pokemon
        interfaces = (graphene.relay.Node,)

    class Query(graphene.ObjectType):

        pokemon = graphene.List(PokemonType)
