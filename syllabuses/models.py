from django.db import models
# Create your models here.
class Syllabus(models.Model):
    _title = models.CharField(max_length=128)
    _des = models.CharField(max_length=1024)
    _type = models.IntegerField(default=0)
    _url = models.CharField(max_length=512)

    def __str__(self):
        return str(self._title)