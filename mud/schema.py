from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Pokemon, Users, Areas

class UserType(DjangoObjectType):
    class Meta:
        model = Users
        interfaces = (graphene.relay.Node,)

class PokemonType(DjangoObjectType):

    class Meta:
        model = Pokemon
        interfaces = (graphene.relay.Node,)

class AreaType(DjangoObjectType):

    class Meta:
        model = Areas
        interfaces = (graphene.relay.Node,)

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        items = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password, items):
        user = Users(
            username=username,
            password=password,
            items=items,
            area_id=0
        )
        return CreateUser(user=user)

class Mutation(graphene.ObjectType,):
    create_user = CreateUser.Field()



class Query(graphene.ObjectType):

    allPokemon = graphene.List(PokemonType)
    pokemon = graphene.Field(PokemonType, pokemonId=graphene.String())
    users = graphene.List(UserType)
    allAreas = graphene.List(AreaType)
    area = graphene.Field(AreaType, areaId=graphene.String())

    def resolve_allPokemon(self, info):
        return Pokemon.objects.all()

    def resolve_pokemon(self, info, **kwargs):
        pokemonId = kwargs.get('pokemonId')
        return Pokemon.objects.get(pk=pokemonId)

    def resolve_users(self, info):
        return Users.objects.all()

    def resolve_allAreas(self, info):
        return Areas.objects.all()

    def resolve_area(self, info, **kwargs):
        areaId = kwargs.get('areaId')
        print(areaId)
        print(kwargs)
        return Areas.objects.get(areaId=areaId)

    def resolve_all_areas(self, info):
        return Areas.objects.all()

    def resolve_area(self, info, **kwargs):
        id = kwargs.get('id')
        return Areas.objects.get(pk=id)

schema = graphene.Schema(query=Query, mutation=Mutation)
