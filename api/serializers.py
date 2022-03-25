from rest_framework.serializers import ModelSerializer

from card.models import Card


class CardSerializer(ModelSerializer):
    """Список карт"""

    class Meta:
        model = Card
        fields = ['series', 'number', 'release_date', 'end_date', 'status']