from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello,word.You're at polls index.")