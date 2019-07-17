from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Pokemon, Users
from django.contrib.auth import get_user_model
import graphql_jwt

class UserType(DjangoObjectType):
    class Meta:
        model = Users
        interfaces = (graphene.relay.Node,)

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        items = graphene.String(required=True)

    def mutate(self, info, username, items):
        user = Users(
            username=username,
            items=items,
            area_id=0
        )
        return CreateUser(user=user)

class Mutation(graphene.ObjectType,):
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

class PokemonType(DjangoObjectType):

    class Meta:
        model = Pokemon
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):

    allPokemon = graphene.List(PokemonType)
    pokemon = graphene.Field(PokemonType, pokemonId=graphene.String())
    users = graphene.List(UserType)

    def resolve_allPokemon(self, info):
        return Pokemon.objects.all()
    
    def resolve_pokemon(self, info, **kwargs):
        pokemonId = kwargs.get('pokemonId')
        return Pokemon.objects.get(pk=pokemonId)

    def resolve_users(self, info):
        return Users.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)