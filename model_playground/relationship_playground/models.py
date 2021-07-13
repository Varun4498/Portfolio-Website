from django.db import models

# Create your models here.

# Many to One Relationship
class Article(models.Model):
    title = models.CharField(max_length = 250)
    body = models.TextField()
    author = models.ForeignKey('Author',on_delete= models.CASCADE)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length = 256)
    designation = models.CharField(max_length = 256) 

    def __str__(self):
        return self.name

# Many to Many Relationship
class Person(models.Model):
    name = models.CharField(max_length = 256)
    socities = models.ManyToManyField('Society', through='Membership')
    def __str__(self):return self.name
class Society(models.Model):
    name = models.CharField(max_length = 256)
    def __str__(self):return self.name
class Membership(models.Model):
    person_id = models.ForeignKey('Person',on_delete=models.CASCADE)
    society_id = models.ForeignKey('Society',on_delete=models.CASCADE)
    designation = models.CharField(max_length = 256)
    #def __str__(self):return self.person_id