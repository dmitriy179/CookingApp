from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "anons", "full_text", "picture", "date"]

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название статьи"
            }),
            "anons": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Анонс статьи"
            }),
            "full_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Текст статьи"
            }),
            "date": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "дата"
            }),
            "picture": FileInput(attrs={
                "class": "form-control",
                "placeholder": "изображение"
            })
        }