from django.db import models

class tiempo(models.Model):
    detalle = models.CharField(max_length=140)
    tiempo_a_medir = models.DateTimeField()

    def __str__(self):
        return self.detalle