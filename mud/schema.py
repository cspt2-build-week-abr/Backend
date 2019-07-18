from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Pokemon, Area, Users, Pokeballs 

class PokemonType(DjangoObjectType):

    class Meta:
        model = Pokemon
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):

    allPokemon = graphene.List(PokemonType)
    pokemon = graphene.Field(PokemonType, pokemonId=graphene.String())

    def resolve_allPokemon(self, info):
        return Pokemon.objects.all()
    
    def resolve_pokemon(self, info, **kwargs):
        pokemonId = kwargs.get('pokemonId')
        return Pokemon.objects.get(pk=pokemonId)


schema = graphene.Schema(query=Query)

