import uuid
from django.db import models


class AbstractModel(models.Model):
    """ Abstract model, used as a parent model """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def deactivate(self):
        self.active = False
        self.save()

    class Meta:
        abstract = True
