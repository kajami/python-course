from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

class Book(models.Model):
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2500),
            MinValueValidator(0)
        ]
    )
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    username = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    addingDate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.name} by {self.author}'

    def get_absolute_url(self):
        return f'/book/{self.pk}'
    
    def delete_object(self):
        return f'/book/delete/{self.pk}'
    
    def update_object(self):
        return f'/book/update/{self.pk}'

