from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Request(models.Model):
    user = models.ForeignKey(User, db_index=True, on_delete=models.PROTECT)
    type = models.CharField(max_length=10, default='GET')
    text = models.CharField(max_length=256, default='')
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(default=now())

    def __str__(self):
        return f'{self.user_id}-{self.type}'
