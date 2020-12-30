from django.db import models

# Create your models here.

class Discussion(models.Model):
    _new = models.IntegerField(default= 0)
    _title = models.CharField(max_length=256)
    _des = models.CharField(max_length=512)

    def __str__(self):
        return "Discussion: " + str(self._title)