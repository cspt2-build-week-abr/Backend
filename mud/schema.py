from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Pokemon, Users, Areas, Pokeballs

class UserType(DjangoObjectType):
    class Meta:
        model = Users
        interfaces = (graphene.relay.Node,)

class PokemonType(DjangoObjectType):

    class Meta:
        model = Pokemon
        interfaces = (graphene.relay.Node,)

class PokeballType(DjangoObjectType):

    class Meta:
        model = Pokeballs
        interfaces = (graphene.relay.Node,)

class AreaType(DjangoObjectType):

    class Meta:
        model = Areas
        interfaces = (graphene.relay.Node,)

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        user = Users(
            username=username,
            password=password,
            items="[]",
            area_id="bde1f21a-4b9f-4993-a7d4-12485402176f",
        )
        user.save()
        return CreateUser(user=user)

class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        userId = graphene.String(required=True)
        username = graphene.String(required=True)
        items = graphene.String(required=True)
        password = graphene.String(required=True)
        area_id = graphene.String(required=True)

    def mutate(self, info, userId, username, items, password, area_id):
        user = Users.objects.get(userId=userId)
        user.username = username
        user.items = items
        user.password = password
        user.area_id = area_id
        user.save()

        return UpdateUser(user=user)

class UpdateArea(graphene.Mutation):
    area = graphene.Field(AreaType)

    class Arguments:
        areaId = graphene.String(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        pokeballs = graphene.String(required=True)
        pokemon = graphene.String(required=True)
        coords = graphene.String(required=True)
        exits = graphene.String(required=True)
        players = graphene.String(required=True)

    def mutate(self, info, areaId, name, description, pokeballs, pokemon, coords, exits, players):
        area = Areas.objects.get(areaId=areaId)
        area.name = name
        area.description = description
        area.pokeballs = pokeballs
        area.pokemon = pokemon
        area.coords = coords
        area.exits = exits
        area.players = players
        area.save()

        return UpdateArea(area=area)

class Login(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def  mutate(self, info, username, password):
        user = Users.objects.get(username=username)
        if user.username == username and user.password == password:
            return Login(user=user)
        else:
            raise Exception("Incorrect username and/or password")

class Mutation(graphene.ObjectType,):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    login = Login.Field()
    update_area = UpdateArea.Field()


class Query(graphene.ObjectType):

    allPokemon = graphene.List(PokemonType)
    pokemon = graphene.Field(PokemonType, pokemonId=graphene.String())
    users = graphene.List(UserType)
    allAreas = graphene.List(AreaType)
    area = graphene.Field(AreaType, areaId=graphene.String())
    user = graphene.Field(UserType, userId=graphene.String())
    allPokeballs = graphene.List(PokeballType)
    pokeball = graphene.Field(PokeballType, pokeballId=graphene.String())

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
        return Areas.objects.get(areaId=areaId)

    def resolve_user(self, info, **kwargs):
        userId = kwargs.get('userId')
        return Users.objects.get(userId=userId)

    def resolve_allPokeballs(self, info):
        return Pokeballs.objects.all()

    def resolve_pokeball(self, info, **kwargs):
        pokeballId = kwargs.get('pokeballId')
        return Pokeballs.objects.get(pokeballId=pokeballId)

schema = graphene.Schema(query=Query, mutation=Mutation)
