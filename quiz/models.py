from django.db import models

# Create your models here.

class Quiz(models.Model):
    topic = models.CharField(max_length=20)
    question = models.TextField()
    answers = models.TextField()
    correct_answers = models.TextField()
