from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
     return render(
        request,
        'SocialLogin/index.html',
        {
            'title':'Social Login ',
            'year':datetime.now().year,     
        }
    )