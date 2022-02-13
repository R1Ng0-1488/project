from rest_framework import serializers 

from .models import AStore, Visit


class AStoreSerializer(serializers.ModelSerializer):
    """Класс сериалайзер Торговых точек"""
    class Meta:
        model = AStore
        fields = ('pk', 'title')


class VisitSerializer(serializers.ModelSerializer):
    """Класс сериалайзер посещений"""

    class Meta:
        model = Visit
        fields = ('astore', 'latitlude', 'longitude')