from django.db import models


class Wordlist4(models.Model):
    word = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wordlist'


class Wordlist6(models.Model):
    word = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wordlist6'


class RankScoreList(models.Model):

    score = models.IntegerField()
    name = models.CharField(max_length=20)


