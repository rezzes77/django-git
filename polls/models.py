from django.db import models

class Clothes(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    price = models.IntegerField()


    def __str__(self):
        return self.name