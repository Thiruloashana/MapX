from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepagee(request):
       # return HttpResponse('<doctype>...')
	return render(request, 'home/homepagee.html')

