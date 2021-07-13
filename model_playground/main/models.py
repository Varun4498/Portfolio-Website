from django.db import models
from django.core.validators import (
    EmailValidator,MaxValueValidator,MinValueValidator,URLValidator,validate_slug # Uniquely identify rows in a database
)

# Create your models here.
# Every table in a database is represented by a class
# Every row in a database is represented by an object of this class
class Student(models.Model):
    GENDERS = (
        ('F','Female'),
        ('M','Male'),
        ('O','Other')
    )
    # varchar(100)
    name = models.CharField(max_length = 100)
    # integer()
    rollno = models.IntegerField(unique= True)
    # text
    # to make null in the ORM as well we give blank = True
    address = models.TextField(null=True)
    phone_number = models.CharField(max_length = 10,null=True,blank = True)
    # validations-(they are callable objects) occur only in ORM level
    emails = models.CharField(max_length = 30,null=True,validators = [EmailValidator("Email address is not valid")])
    gender = models.CharField(max_length = 1, choices = GENDERS,null=True)
    age = models.IntegerField(null=True,validators=[
        MaxValueValidator(125),
        MinValueValidator(0),
    ])
    slug = models.CharField(max_length = 100 , validators = [validate_slug],null = True)
    # Dunder Function
    def __str__(self):
        return self.name