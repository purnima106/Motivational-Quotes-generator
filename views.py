from django.shortcuts import render
from requests import *

def home(request):
		if request.GET.get("btn"):
			url = "http://api.quotable.io/random"
			res = get(url)
			data = res.json()
			msg = data["content"]
			return render(request, "home.html", {"msg":msg})
		else:
			return render(request, "home.html")