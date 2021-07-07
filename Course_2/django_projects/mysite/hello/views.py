from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def myview(request):
    visits = request.session.get('num_visits',0) + 1
    request.session['num_visits'] = visits
    if visits>4 :
        del(request.session['num_visits'])
    resp = HttpResponse("view count="+str(visits))
    resp.set_cookie('dj4e_cookie', 'd5133640', max_age=1000)
    return resp