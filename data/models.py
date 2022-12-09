from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    # image = models.ImageField(upload_to= 'media/')
    email = models.EmailField()
    password = models.CharField(max_length=200, null=False)
    

    def __str__(self):
        return self.name 