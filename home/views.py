from django.shortcuts import render,HttpResponse
from . import models
import uuid

from .sendsms import sendsms

from django.core.mail import send_mail
# views.py
from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def candidateaura(request):
    allTasks = models.Candidateaura.objects.all()
    context = {'task': allTasks}
    return render(request,'candidateaura.html',context)

def candidatepalg(request):
    allTasks = models.Candidatepalg.objects.all()
    context = {'task': allTasks}
    return render(request,'candidatepalg.html',context)

def amroha(request):
    success = False
    x=1
    context = {'success': success, 'uid': x}
    print(success)
    if request.method == "POST":
        if request.POST.get('name'):
            print("yesss")
            name = request.POST['name']
            age = int(request.POST['age'])
            address = request.POST['address']
            pannumber = request.POST['pannumber']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            constituency = "Amroha"
            allTasks = models.Votergovt.objects.all()
            x = str(uuid.uuid1())
            x=str(x[0:10])
            # send_mail(
            #     'UID Generated for evoting',
            #     x,
            #     'noreplyvamp@yahoo.com',
            #     [email],
            #     fail_silently=False,
            # )

            ins2 = models.UIDamroha(pannumber=pannumber, uniqueid=x)
            ins = models.Voterregisteredamroha(name=name, age=age, address=address, pannumber=pannumber, email=email,phonenumber=phonenumber)
            if (models.Votergovt.objects.filter(name=name, pannumber=pannumber,constituency=constituency).exists())and (not models.Voterregisteredamroha.objects.filter(name=name,pannumber=pannumber).exists())and(age>=18):
                ins.save()
                success = True
                ins2.save()
                y="+91"+str(phonenumber)
                sendsms(mess=x,ph=y)
                context = {'success': success, 'uid': x}

            else:
                 success = False
        if request.POST.get('uid'):
            print('form 2')
            uniqueid=str(request.POST['uid'])
            pannumber=str(request.POST['pan'])
            if models.UIDamroha.objects.filter(uniqueid=uniqueid,pannumber=pannumber).exists():
                print("Yes you are on correct page")
                allTasks = models.Candidateaura.objects.all()
                context={'task':allTasks}
                return render(request,'voteaura.html',context)
        if request.POST.get('phonenumber2'):
            print('form 2')
            phonenumber=request.POST['phonenumber2']
            pannumber=str(request.POST['pan2'])
            name=str(request.POST['name2'])
            if models.Voterregisteredamroha.objects.filter(pannumber=pannumber,name=name):
                UIDN=models.UIDamroha.objects.all()
                context={'task':UIDN}
                return render(request,'')

    return render(request,'amroha.html',context)

def palghar(request):
    success = False
    x=1
    context = {'success': success, 'uid': x}
    print(success)
    if request.method == "POST":
        if request.POST.get('name'):
            print("yesss")
            name = request.POST['name']
            age = int(request.POST['age'])
            address = request.POST['address']
            pannumber = request.POST['pannumber']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            constituency = "Palghar"
            allTasks = models.Votergovt.objects.all()
            x = str(uuid.uuid1())
            x=str(x[0:10])
            # send_mail(
            #     'UID Generated for evoting',
            #     x,
            #     'noreplyvamp@yahoo.com',
            #     [email],
            #     fail_silently=False,
            # )

            ins2 = models.UIDpalghar(pannumber=pannumber, uniqueid=x)
            ins = models.Voterregisteredpalghar(name=name, age=age, address=address, pannumber=pannumber, email=email,phonenumber=phonenumber)
            if (models.Votergovt.objects.filter(name=name, pannumber=pannumber,constituency=constituency).exists())and (not models.Voterregisteredpalghar.objects.filter(name=name,pannumber=pannumber).exists())and(age>=18):
                ins.save()
                success = True
                ins2.save()
                y = "+91" + str(phonenumber)
                sendsms(mess=x, ph=y)
                context = {'success': success, 'uid': x}

            else:
                 success = False
        if request.POST.get('uid'):
            print('form 2')
            uniqueid=str(request.POST['uid'])
            pannumber=str(request.POST['pan'])
            if models.UIDpalghar.objects.filter(uniqueid=uniqueid,pannumber=pannumber).exists():
                print("Yes you are on correct page")
                allTasks = models.Candidatepalg.objects.all()
                context={'task':allTasks}
                return render(request,'votepalg.html',context)

    return render(request,'palghar.html',context)