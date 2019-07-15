from rest_framework import serializers
from mud.models import Areas
from mud.models import Users
from mud.models import Pokemon
from mud.models import Pokeballs

class areaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class pokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

class pokeballSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokeballs
        fields = '__all__'
