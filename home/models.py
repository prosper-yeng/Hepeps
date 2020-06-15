from django.db import models

# Create your models here.

class HepepsTeam(models.Model):
    # name = models.CharField(max_length=200)
    # img = models.ImageField(upload_to='pics')
    # Desc = models.TextField()
    # Read_more = models.CharField(max_length=200)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    other_names = models.CharField(max_length=200, null=True, blank=True)
    img_url = models.FileField(upload_to='pics')
    Bio = models.TextField()
    role = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'Hepeps Team'


class BackgroundImages(models.Model):
    img_url = models.FileField(upload_to='pics')
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'Background Images'


