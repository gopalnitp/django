from django.http import HttpResponse
#from __future__ import unicode_literals

from django.shortcuts import render
#from django.http import HttpResponse
def homepage(request):
	return render(request,'homepage.html')



#def name(request):
#	return HttpResponse('Gopal')
