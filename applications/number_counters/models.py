from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import NumberCounterManager


class NumberCounter(models.Model):
    """
    NumberCounter model.
    """
    number = models.IntegerField(
        verbose_name=_('number'),
        help_text=_('Number for analyze.'),
        unique=True,
    )
    count = models.PositiveIntegerField(
        verbose_name=_('count'),
        help_text=_('Count analyzed numbers.'),
        default=1,
    )

    objects = NumberCounterManager()

    def __str__(self):
        return 'number: {number}, count: {count}'.format(
            number=self.number,
            count=self.count,
        )
