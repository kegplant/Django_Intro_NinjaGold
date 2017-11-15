from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from locations import locations
import random

#helper functions
def loot(location_id):
    print 'looting'
    gain=random.randrange(locations[int(location_id)-1]['min'],locations[int(location_id)-1]['max'])
    return gain
def log(location_id,gain):
    print 'logging'
    gain=int(gain)
    if gain>=0:
        activity='Earned {} golds from the {}! ({})'.format(gain,locations[int(location_id)-1]['name'],datetime.now())
    else:
        activity='Entered a casino and lost {} golds... Ouch.. ({})'.format(gain,datetime.now())
    return activity
def handleErrors(request):
    try:
        request.session['activities']
    except:
        request.session['activities']=[]
    try:
        request.session['totalGold']
    except:
        request.session['totalGold']=0
    try:
        request.session['color']
    except:
        request.session['color']=[]
    return
# the index function is called when root is visited
def index(request):
    handleErrors(request)
    context={
        'locations': locations,
        'activities': zip(request.session['color'],request.session['activities'])
    }
    return render(request,'ninja_gold/index.html',context)
def process(request,location_id):
    handleErrors(request)
    print 'processing'
    gain=loot(location_id)
    activity=log(location_id,gain)
    if int(gain) >=0:
        request.session['color'].append('green')
    else:
        request.session['color'].append('red')
    request.session['totalGold']+=gain
    request.session['activities'].append(activity)
    request.session.modified = True
    # print " Ninja was here!"
    return redirect('/')
def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
