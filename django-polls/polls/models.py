import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    @admin.display(boolean=True, ordering="pub_date", description="Published recently?")
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    @admin.display(boolean=True, description="Will be published in the future?")
    def to_be_published(self):
        now = timezone.now()
        return self.pub_date >= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.choice_text + " " + str(self.votes)
