from django.shortcuts import render
#from django.http import HttpResponse
from first_app.models import AccessRecore, Topic, Webpage

# Create your views here.

def index(request):
    webpage_list = AccessRecore.objects.order_by('date')
    data_dict = {'access_record':webpage_list}
    return render(request,'first_app_templates/index.html', context=data_dict)
