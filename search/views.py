from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .qsort import *


# Create your views here.
@csrf_exempt
def searchhome(request):
  if request.method == "POST":
    arr=(request.POST.getlist('d[]'))
    n = len(arr) 
    quickSort(arr,0,n-1)
    print(arr)
    return JsonResponse({'sorteddata':arr})

  return render(request,'search.html')

