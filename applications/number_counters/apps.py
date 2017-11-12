from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NumberCountersConfig(AppConfig):
    name = 'applications.number_counters'
    label = 'number_counters'
    verbose_name = _('number counters')
