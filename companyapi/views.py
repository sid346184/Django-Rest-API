from django.http import HttpResponse


def homepage(request):
    print("Home page")
    return HttpResponse("HELLO")






