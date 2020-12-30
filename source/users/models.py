import sys
sys.path.insert(0, '')
from ..courses.models import Course

from django.db import models


# Create your models here.
class User(models.Model):
    _name = models.CharField(max_length=256)
    _username = models
    _email = models.EmailField(max_length=255, unique= True)
    _birthday = models.DateField()

class User_Course(models.Model):
    _user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    _course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    _join_date = models.DateField()

class User_Submission(models.Model):
    _user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    _quiz_id = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    _submit_date = models.DateTimeField()
    _status = models.IntegerField(default= 0)
    # _status:
    #  = 0: time remained
    #  = 1: submitted
    #  = 2: overdue