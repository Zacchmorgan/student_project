from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=50)
    csuid = models.CharField(max_length=10)
    mobile = models.CharField(max_length=14)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)