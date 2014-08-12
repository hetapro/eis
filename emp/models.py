from django.db import models

class Emp1(models.Model):
    ename=models.CharField(max_length=200)
    age=models.IntegerField(default=0)
    emailid=models.EmailField(max_length=200)
    mobno=models.IntegerField()
    designation=models.CharField(max_length=20)

class Dep(models.Model):
    emp1=models.ForeignKey(Emp1)
    dept=models.CharField(max_length=200)