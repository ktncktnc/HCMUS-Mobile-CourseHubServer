from django.db import models

# Create your models here.
class Quiz(models.Model):
    _title = models.CharField(max_length=128)
    _des = models.CharField(max_length=1024)
    _count = models.DateTimeField()
    
    def __str__(self):
        return "Quiz: " + str(self._title)