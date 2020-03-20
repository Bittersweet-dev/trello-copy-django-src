from rest_framework import serializers
from .models import Example

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
        )
        model = Example
