# models.py

from django.db import models

class SlideImage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel_images/')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
