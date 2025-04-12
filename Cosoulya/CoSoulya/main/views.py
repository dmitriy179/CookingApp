from django.shortcuts import render
def main(request):
    dict_ = {
        "title": "Главная страница"
    }
    return render(request, "main/main.html", dict_)

def registration(request):
    return render(request, "main/registration.html")


