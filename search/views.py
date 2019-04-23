from django.shortcuts import render

# Create your views here.
def searchhome(request):
	return render(request,'search.html')

