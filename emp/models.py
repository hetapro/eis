from django.db import models

class Dep(models.Model):
    dept=models.CharField(max_length=200)

    def __unicode__(self):
        return self.dept

class Emp1(models.Model):
    ename=models.CharField(max_length=200)
    age=models.IntegerField(default=0)
    emailid=models.EmailField(max_length=200)
    mobno=models.IntegerField()
    designation=models.CharField(max_length=20)
    dep=models.ForeignKey(Dep, on_delete=models.CASCADE)

