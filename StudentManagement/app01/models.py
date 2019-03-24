from django.db import models


# Create your models here.

class Classes(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Students(models.Model):
    sname = models.CharField(max_length=32)
    gender = models.CharField(max_length=10)
    classes = models.ForeignKey('Classes', on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

class Teachers(models.Model):
    tname = models.CharField(max_length=32)
    # gender = models.CharField(max_length=10)
    # age = models.IntegerField()

class Courses(models.Model):
    cname = models.CharField(max_length=32)
    teacher = models.ForeignKey('Teachers',on_delete=models.CASCADE)
    student = models.ManyToManyField('Students')

    def __str__(self):
        return self.cname


class Score(models.Model):
    number = models.IntegerField()
    student = models.ForeignKey('Students')
    course = models.ForeignKey('Courses')

