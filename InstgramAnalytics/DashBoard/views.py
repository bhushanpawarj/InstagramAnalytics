from django.shortcuts import render
from datetime import datetime
import requests
import json
import time
# Create your views here.
def index(request):

     #code = request.GET.get("access_token")
     user = request.user
     social = user.social_auth.get(provider='instagram')
     access_token=social.access_token

     #creating request to get followers and following details
     response = requests.get("https://api.instagram.com/v1/users/self/?access_token="+access_token)
     if(response.ok):
                jData = json.loads(response.content)
                follows=jData['data']['counts']['follows']
                followed_by=jData['data']['counts']['followed_by']
                media_count=jData['data']['counts']['media']
     else:
            # If response code is not ok (200), print the resulting http error code with description
            response.raise_for_status()

    #now creating Date and likes arrays
     Dates=[]
     Likes=[]
     response = requests.get("https://api.instagram.com/v1/users/self/media/recent/?access_token="+access_token)
     if(response.ok):
                jData = json.loads(response.content)
                for data in jData['data']:
                   #timeStamp = time.gmtime(int(data['created_time']))
                   #Dates.append( timeStamp)
                   #Dates.append(time.strftime("%Y-%m-%d", timeStamp))
                   #temp=datetime.fromtimestamp(int(data['created_time'])).strftime('%c')
                   timeStamp = time.gmtime(int(data['created_time']))
                   temp=time.strftime("%Ytemp", timeStamp)
                   temp1=temp.__repr__()
                   #temp1=temp1.decode('unicode_escape').encode('ascii','ignore')
                   Dates.append(int(data['created_time']))
                   Likes.append(data['likes']['count'])
     else:
            # If response code is not ok (200), print the resulting http error code with description
            response.raise_for_status()


     #Per tag likes 
     response = requests.get("https://api.instagram.com/v1/users/self/media/recent/?access_token="+access_token)
     if(response.ok):
                jData = json.loads(response.content)
                for data in jData['data']:
                   timeStamp = time.gmtime(int(data['created_time']))
                   temp=time.strftime("%Ytemp", timeStamp)
                   temp1=temp.__repr__()
                   #temp1=temp1.decode('unicode_escape').encode('ascii','ignore')
                   Dates.append(int(data['created_time']))
                   Likes.append(data['likes']['count'])
     else:
            # If response code is not ok (200), print the resulting http error code with description
            response.raise_for_status()

     return render(
        request,
        'DashBoard/index.html',
        {
            'title':'DashBoard ',
            'year':datetime.now().year, 
            'follows':follows,
            'followed_by':followed_by,
            'media_count':media_count,
            'Dates' : Dates,
            'Likes':json.dumps(Likes),
            'access_token':access_token,
        }
    ) 
