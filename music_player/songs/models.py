from django.db import models

# Create your models here.

class Song(models.Model):
	artist = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	url = models.URLField()

	def __str__(self):
		return '{} by {}'.format(self.name, self.url)

	def to_dict(self):
		return {
    		'name': self.name,
    		'artist': self.artist,
    		'url': self.url
    	}

