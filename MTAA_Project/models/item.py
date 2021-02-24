from MTAA_Project.models.abstract_model import AbstractModel
from django.db import models


class Item(AbstractModel):
    brand = models.TextField()
    model = models.TextField()
    color = models.TextField()
    status = models.TextField()
    description = models.TextField()
    gps_lat = models.FloatField(null=True, blank=True, verbose_name='GPS Latitude', help_text='Napr.: 49.099426', )
    gps_lon = models.FloatField(null=True, blank=True, verbose_name='GPS Longitude', help_text='Napr.: 19.539846', )

    class Meta:
        db_table = 'item'
