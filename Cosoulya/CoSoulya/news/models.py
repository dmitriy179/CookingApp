from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField("Название", max_length=50)
    anons = models.CharField("Подпись", max_length=150)
    full_text = models.TextField("Статья")
    date = models.DateTimeField("Дата публикации")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"



