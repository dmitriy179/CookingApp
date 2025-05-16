from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["name", "password"]

        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имя"
            }),
            "password": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Пароль"
            })
        }