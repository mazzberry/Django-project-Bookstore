from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

class books(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)# adad gheymat (XXXXX.XX = 2 ashar, 5 adad)

    book_cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class comments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(books, on_delete=models.CASCADE, related_name='comments')

    text = models.TextField()

    datetime_created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.text





