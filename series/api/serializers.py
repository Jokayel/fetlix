from typing import Dict

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from series.models import Serie


class SerieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    def validate(self, serie: Dict[str, str]):
        if not serie.get('title'):
            raise ValidationError('title is mandatory')
        return serie

    class Meta:
        model = Serie
        fields = '__all__'
