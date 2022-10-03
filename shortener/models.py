from django.db import models

# Create your models here.
class UrlsDatabase(models.Model):
    url = models.TextField(max_length=10000, primary_key=True)
    uuid = models.CharField(max_length=10,unique=True)
    url_visit_count=models.IntegerField(default=0)