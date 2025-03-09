from django.db import models
import uuid

class Wallet(models.Model):
    id_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.IntegerField()

    def __str__(self):
        return f'{self.id_uuid}: {self.balance}'