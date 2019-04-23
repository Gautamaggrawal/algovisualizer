from django.shortcuts import render
import json

# Create your views here.
def home(request):
	
	
	python_object = {
	"name": "Top Level",
	"parent": "null",
	"children": [
	{
	"name": "Level yosh: A",
	"parent": "Top Level",
	"children": [
	{
	"name": "Son of A",
	"parent": "Level 2: A"
	},
	{
	"name": "Daughter of A",
	"parent": "Level 2: A"
	}
	]
	},
	{
	"name": "Level 2: B",
	"parent": "Top Level"
	}
	]}
	json_string = json.dumps(python_object)
	return render(request, 'bst/bst.html' , {'json_string': json_string})


def tryq(request):
	a=[]
	if request.method=='POST':
		print(request.POST.get('node'))
		a.append(request.POST.get('node'))
		print(a)
	
	return render(request, 'bst/bst1.html' , {'s':a})
