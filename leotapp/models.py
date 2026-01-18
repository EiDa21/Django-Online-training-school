from django.db import models

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length= 500)
    Email = models.EmailField(max_length= 100)
    Message = models.TextField()

    def __str__(self) -> str:
        return self.Name

class Register(models.Model):
    name = models.CharField(max_length= 500)
    email = models.EmailField(max_length= 100)
    phone_number = models.IntegerField()
    courses = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

