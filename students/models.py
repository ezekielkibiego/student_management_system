from django.db import models
from cloudinary.models import CloudinaryField

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    profile_image = CloudinaryField('image', blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"