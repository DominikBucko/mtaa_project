from django.db import models
from MTAA_Project.models.abstract_model import AbstractModel


class User(AbstractModel):

    email = models.TextField()

    class Meta:
        db_table = 'user'
