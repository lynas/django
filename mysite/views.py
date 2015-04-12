from django.shortcuts import render_to_response
from mysite.models import Line
#from mysite.models import UsersOfIpv


def home(request):
    # line = Line(text="testing line one")
    #line.save()
    # user_of_ipv = UsersOfIpv(title="test", body="body")
    # user_of_ipv.save()

    print Line.objects.all()
    return render_to_response("mysite/home.html", {'lines': Line.objects.all()})

