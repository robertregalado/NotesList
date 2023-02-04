from rest_framework import serializers
from .models import Notelist


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notelist
        fields = ('id', 'task', 'description', 'completed', 'created')