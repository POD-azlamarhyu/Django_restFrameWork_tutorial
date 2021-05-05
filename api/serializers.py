from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinckedModelSerializer):
    class Meta:
        model = Todo
        fields = ('title','text','id','created_at')

