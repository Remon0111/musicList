from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Music(models.Model):
    id = models.BigAutoField(primary_key=True)
    musicname = models.CharField(max_length=200)
    musicvocalist = models.CharField(max_length=200)
    musicimages = models.CharField(max_length=200)
    albumname = models.CharField(max_length=200)
    musicurl = models.CharField(max_length=200)
    musicselect = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.musicname

    class Meta:
        db_table = 'music_list'