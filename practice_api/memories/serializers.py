from rest_framework import serializers
from .models import *

class MemoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Memories
        fields = ['id', 'text', 'pub_date', 'owner']
        read_only_fields = ('owner',)