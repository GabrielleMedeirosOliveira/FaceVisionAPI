from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

class DefaultReturns:
    @csrf_exempt
    def hello_world(request):
        if request.method == 'GET':
            return HttpResponse('Hello World')
        elif request.method == 'POST':
            return HttpResponse(status=200)

# Create your views here.
