from django.db import models

# Create your models here.
class Wpis(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # dodaj miniaturke do wpisu - to robimy potem
    # dodaj autora do wpisu - to robimy potem

    def __str__(self):
        return self.title

    def przycinanie(self):
        return self.body[:50] + '...'

