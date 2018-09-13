from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import requests
import simplejson as json



# Create your views here.
def index(request):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    #sending api request 
    search_clicked=request.POST.get('tag')
    jData={ 'data' : ''}
    if search_clicked =='' or search_clicked ==None:
        jData={ 'data' : ''}
    else :
        response = requests.get("https://api.instagram.com/v1/tags/search?q=+" + search_clicked+"&access_token=1507486508.8923420.bd890a9986174a05a54d17e5f9d6e8f0&count=50")
        if(response.ok):
                jData = json.loads(response.content)
                print("The response contains {0} properties".format(len(jData)))
                for item in jData['data']:
                    try :
                        print(item)
                    except :
                        print(str(item).encode("unicode_escape"))
        else:
            # If response code is not ok (200), print the resulting http error code with description
            response.raise_for_status()
 

    return render(
        request,
        'Search/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'jData' : jData['data'],
            'lengthOfDictonary' : len(jData['data']),
            'search_clicked' :search_clicked,
            
        }
    )


#doownload album 

def download(request,tag_name='followforfollow'):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    #sending api request 
    tag_name=tag_name
    jData={ 'data' : ''}
    search_clicked=request.POST.get('tag')
 
    response = requests.get("https://api.instagram.com/v1/tags/picoftheday/media/recent?access_token=1507486508.8923420.bd890a9986174a05a54d17e5f9d6e8f0&count=10")
    if(response.ok):
                jData = json.loads(response.content)
                print("The response contains {0} properties".format(len(jData)))
                for item in jData['data']:
                    try :
                        print(itemitem['images']['standard_resolution']['url'])
                    except :
                        print(str(itemitem['images']['standard_resolution']['url']).encode("unicode_escape"))
    else:
            # If response code is not ok (200), print the resulting http error code with description
            response.raise_for_status()
 

    return render(
        request,
        'Search/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'jData' : jData['data'],
            'lengthOfDictonary' : len(jData['data']),
            'search_clicked' :search_clicked,
            'tag_name' : tag_name,
            
        }
    )

#Show Album
def ShowAlbum(request,TagName):
    """Renders the home page."""
    
 

    return render(
        request,
        'Search/Media.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'tag_name' : TagName,

            
        }
    )

