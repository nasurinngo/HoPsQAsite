from django.db import models
from .consts import MAX_RATE
# Create your models here.

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

CATEGORY = (('campusLife', '学校生活'), ('class', '授業'), ('part-timeJob', 'アルバイト'), ('club', 'サークル活動'),('dreamProject', '夢プロジェクト'), ('entranceExamination', '入試'), ('study', '勉強'), ('seminar', 'ゼミ'), ('departmentalSelection', '学科選択'), ('other', 'その他'), ('wanted', '現在回答募集中の質問'))

class HoPs(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
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