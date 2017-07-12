from django.db import models
from django.conf import settings


class Verse(models.Model):
    reference = models.CharField(primary_key=True, max_length=100)
    text = models.TextField()


class WordStudy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='word_studies')
    title = models.CharField(max_length=300)


class WordStudyCategory(models.Model):
    DEFAULT_CATEGORY = 'Uncategorized'

    title = models.CharField(max_length=300)
    study = models.ForeignKey(WordStudy, on_delete=models.CASCADE, related_name='categories')


class WordStudyNote(models.Model):
    note = models.TextField(default='')
    category = models.ForeignKey(WordStudyCategory, on_delete=models.CASCADE, related_name='notes')
    verse = models.ForeignKey(Verse, on_delete=models.DO_NOTHING, related_name='+')
