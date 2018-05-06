from django.shortcuts import render
from django.http import JsonResponse
import datetime
import time

def index(request):
    return render(request,'index.html',{

    })

def display(request, month, day, year):
    date = datetime.datetime(int(month),int(day),int(year))
    timestamp = time.mktime(date.timetuple())
    return JsonResponse(timestamp, safe=False)

def display1(request,id):
    print ('id',id)
    datestring = id
    dt = datetime.datetime.fromtimestamp(float(datestring))
    print(dt)
    return JsonResponse(dt,safe=False)