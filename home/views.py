from django.shortcuts import render

# Create your views here.

#direction to homepage

def home(request):
	return render(request,"index.html",{})