from django.shortcuts import render_to_response

def home(request):
	return render_to_response("mysite/home.html", {'hello': "hello world"})

