from django.shortcuts import render,HttpResponseRedirect,HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def BinarySearchTreeView(request):
	if request.method=='POST':
		arr=(request.POST.getlist('d[]'))
		arr=list(map(int, arr))
		return JsonResponse({'data': arr})

	return render(request, 'bst/bst.html')