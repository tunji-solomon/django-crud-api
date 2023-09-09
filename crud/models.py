from django.db import models

class Phones(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.name
class Gender(models.Model):
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.gender
    
class Student(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    sex = models.ForeignKey(Gender, on_delete= models.CASCADE)
    dob = models.DateField()

    def __str__(self):
        return f'{self.f_name}   {self.l_name}'

