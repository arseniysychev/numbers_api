import collections

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from .models import NumberCounter


class UnpairedSerializer(serializers.Serializer):
    data = serializers.ListField(
        write_only=True,
        child=serializers.IntegerField(),
    )

    answer = serializers.SerializerMethodField(
        read_only=True,
    )

    def __init__(self, *args, **kwargs):
        super(UnpairedSerializer, self).__init__(*args, **kwargs)
        self.counter_from_data = collections.Counter(self.initial_data['data'])
        self.odd_list = None

    def get_answer(self, obj):
        return obj.number

    def validate_data(self, value):
        if not value:
            raise serializers.ValidationError(_('Can\'t be empty list.'))

        self.odd_list = tuple((key, count) for key, count in self.counter_from_data.items() if count % 2 != 0)

        if not self.odd_list:
            raise serializers.ValidationError(_('Data list not include odd value.'))

        if len(self.odd_list) > 1:
            raise serializers.ValidationError(_('Too many odd values.'))

        return value

    def create(self, validated_data):
        return NumberCounter.objects.accumulate_number(self.odd_list[0][0], self.odd_list[0][1])

    def update(self, instance, validated_data):
        pass


class NumberCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberCounter
        fields = ('number', 'count')
