from django.conf.urls import url

from applications.number_counters.views import UnpairedAPIView, StatisticAPIView

urlpatterns = [
    url(r'^unpaired/', UnpairedAPIView.as_view(), name='send_unpaired'),
    url(r'^statistic/', StatisticAPIView.as_view(), name='get_statistic'),
]
