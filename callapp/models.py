from django.db import models

# Create your models here.
class CallLog(models.Model):
    id = models.IntegerField(primary_key=True)
    from_number=models.CharField(max_length=10,null=True)
    to_number=models.CharField(max_length=10,null=True)
    calling_time=models.TimeField()