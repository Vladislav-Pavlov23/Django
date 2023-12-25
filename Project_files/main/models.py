from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField('Назва', max_length=500)
    anons = models.CharField('Анонс', max_length=2550)
    full_text = models.TextField('Стаття')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статті'
        verbose_name_plural = 'Новини'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username