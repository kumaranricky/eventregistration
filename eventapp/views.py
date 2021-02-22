from django.shortcuts import render
from .models import participant
# Create your views here.
def home(request):
    context = {}
    return render(request,'eventapp/home.html',context)
def register(request):
    context = {}
    if request.method == 'POST':
        p1 = participant()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.phone = request.POST.get('phone','000')
        p1.institution = request.POST.get('institution','-')

        if len(participant.object.all()) > 10:
            return render(request, 'eventapp/failed.html', context)
        else:
            p1.save()
            return render(request, 'eventapp/success.html', context)

    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['institution'] = ''

    return render(request, 'eventapp/register.html', context)

def listofparticipant(request):
    context = {}

    context['participant'] = participant.objects.all()

    return render(request, 'eventapp/listofparticipant.html', context)

def success(request):
    context = {}
    return render(request,'eventapp/success.html',context)

def failure(request):
    context = {}
    return render(request,'eventapp/failure.html',context)