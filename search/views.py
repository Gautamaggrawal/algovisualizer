from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .qsort import *


@csrf_exempt
def SortingView(request):
  if request.method == "POST":
    arr=(request.POST.getlist('d[]'))
    n = len(arr) 
    quickSort(arr,0,n-1)
    return JsonResponse({'sorteddata':arr})

  return render(request,'search.html')

