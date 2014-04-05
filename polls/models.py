import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    fun_stuff = models.CharField(max_length=420)

    def __unicode__(self):
        return self.question_text

    def was(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(minutes=1)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(minutes=1)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
