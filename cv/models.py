from django.db import models

class ContactDetails(models.Model):
    text = models.TextField(default='')

class Education(models.Model):
    start = models.TextField(default='')
    end   = models.TextField(default='')
    qual  = models.TextField(default='')
    inst  = models.TextField(default='')
    grade = models.TextField(default='')
