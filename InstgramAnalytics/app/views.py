"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.core.mail import send_mail
from . import models 

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    if request.method=="POST":
        form_sender=request.POST.get('name')
        form_email=request.POST.get('email')
        form_subject=request.POST.get('subject')
        form_message=request.POST.get('message')
        #form_message=form_message+"\n From - " + form_email + "\n Name Of Sender -" +form_sender 
        #store these into database instead of sending  via mail 
        user=models.User(Name=form_sender ,Email=form_email,Subject=form_subject,Message=form_message,Time=datetime.now())
        try :
            user.save()
            Result=True
        except:
            Result=False

        #send_mail_response=send_mail(form_subject ,form_message  , form_email ,["xbhushanpawarx@gmail.com"] ,fail_silently=True)
        return render(
            request,
            'app/contact.html',
            {
                'title':'Contact',
                'message':'Your contact page.',
                'year':datetime.now().year,
                'Result':Result,
            }
        )
    
    else :
        return render(
            request,
            'app/contact.html',
            {
                'title':'Contact',
                'message':'Your contact page.',
                'year':datetime.now().year,
            }
        )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
