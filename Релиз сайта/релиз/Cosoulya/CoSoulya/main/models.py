from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField("Имя", max_length=50)
    anons = models.CharField("Пароль", max_length=150)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"



