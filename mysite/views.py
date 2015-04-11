from django.shortcuts import render_to_response
from mysite.models import Line


def home(request):
    line = Line(text="testing line one")
    line.save()
    return render_to_response("mysite/home.html", {'hello': "hello world"})

