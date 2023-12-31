from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    duration = models.IntegerField()
    last_play = models.DateField()

    def __str__(self):
        return self.title
