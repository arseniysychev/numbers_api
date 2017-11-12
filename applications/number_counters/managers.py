from django.db import models, IntegrityError


class NumberCounterManager(models.Manager):
    """
    Manager fo NumberCounter model.
    """

    def accumulate_number(self, number, count):
        """
        Create or update NumberCounter item.
        """
        try:
            obj = self.create(number=number)
        except IntegrityError:
            obj = self.get(number=number)
            obj.count = models.F('count') + count
            obj.save()
        return obj
