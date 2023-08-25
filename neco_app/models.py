from typing import Any
from django.db import models

# Create your models here.

class Detail(models.Model):
    building = models.CharField(max_length=1, choices=[('A', 'Building A'), ('B', 'Building B')],blank=True,null=True)
    floor = models.PositiveIntegerField(blank=True,null=True)
    room_number=models.PositiveIntegerField()
    owner_name=models.CharField(max_length=50)
    member=models.IntegerField()
    mobile_number=models.CharField(max_length=11)

    def __str__(self):
        return  self.building 