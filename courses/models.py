from django.db import models
from ..quizzes.models import Quiz
from ..syllabuses.models import Syllabus
from ..discussions.models import Discussion
# Create your models here.
class Course(models.Model):
    _title = models.CharField(max_length=256)
    _avt = models.CharField(max_length=512)
    _teacher = models.CharField(max_length=64)
    _ta1 = models.CharField(max_length=64)
    _ta2 = models.CharField(max_length=64)
    _description = models.CharField(max_length=512)
    _syllabuses = models.CharField(max_length=1024)

    def _str__(self):
        return str(self._title) + " teacher: " + str(self._teacher)

class Course_Quiz(models.Model):
    _course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    _quiz_id = models.ForeignKey(Quiz, on_delete = models.CASCADE)

class Course_Syllabus(models.Model):
    _course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    _syllabus_id = models.ForeignKey(Syllabus, on_delete = models.CASCADE)
    
class Course_Discussion(models.Model):
    _course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    _discussion_id = models.ForeignKey(Discussion, on_delete = models.CASCADE)

