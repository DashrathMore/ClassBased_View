from django.db import models

# Create your models here.

class student(models.Model):
    srn = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.sname
