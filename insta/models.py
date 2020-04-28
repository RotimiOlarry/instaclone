from django.db import models
from django.utils import timezone

# Create your models here.
def post(models.Model):
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    image = models.ImageField(bland = True,null = True)
    caption = models.TextField()
    created_date = models.DateTimeField(defualt = timezone.now)
