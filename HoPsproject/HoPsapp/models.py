from django.db import models
from .consts import MAX_RATE
# Create your models here.

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

CATEGORY = (('１年生', '１年生'), ('２年生', '２年生'), ('３年生', '３年生'))

class HoPs(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    category = models.CharField(
            max_length=100,
            choices = CATEGORY
            )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    HoPsapp = models.ForeignKey(HoPs, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title