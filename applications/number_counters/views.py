from rest_framework.generics import ListAPIView, CreateAPIView

from .models import NumberCounter
from .serializers import UnpairedSerializer, NumberCounterSerializer


class UnpairedAPIView(CreateAPIView):
    """
    API View for send data list via POST method.
    """
    serializer_class = UnpairedSerializer


class StatisticAPIView(ListAPIView):
    """
    API View for get statistic.
    """
    queryset = NumberCounter.objects.all()
    serializer_class = NumberCounterSerializer
