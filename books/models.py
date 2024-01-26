from django.db import models

# Create your models here.

class books(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)# adad gheymat (XXXXX.XX = 2 ashar, 5 adad)

    def __str__(self):
        return self.title
