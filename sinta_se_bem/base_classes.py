from uuid import uuid4
from django.db import models


class GenericWithUUID(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True
