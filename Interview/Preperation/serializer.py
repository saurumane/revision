from rest_framework import serializers
from .models import Userinputmodel
class Userser(serializers.ModelSerializer):
    class Meta:
        model=Userinputmodel
        fields= "__all__"