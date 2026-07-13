from django.db import models

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(blank=False, null = False)
    lastname = models.CharField(blank=False, null = False)
    school_name = models.CharField(blank=False, null = False)
    age = models.PositiveIntegerField(blank=False, null = False)
    created_at = models.DateTimeField(auto_now_add=True)