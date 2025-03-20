from django.http import HttpResponse

# Create your views here.

def star(request):
    return HttpResponse('app is running')