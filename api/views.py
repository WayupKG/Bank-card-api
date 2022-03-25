from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from card.models import Card
from .serializers import CardSerializer


class CardAPIView(APIView):
    """Вывод списка карт"""
    def get(self, request):
        card = Card.active.all()
        serializer = CardSerializer(card, many=True)
        return Response(serializer.data)