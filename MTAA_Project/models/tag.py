from django.db import models
from MTAA_Project.models.abstract_model import AbstractModel


class Tag(AbstractModel):

    tag_name = models.TextField()

    class Meta:
        db_table = 'tag'
        verbose_name = 'tag'
