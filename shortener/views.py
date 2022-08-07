from django.forms import ValidationError
from django.shortcuts import redirect, render
from shortener.form import UrlForm
import uuid
from shortener.models import UrlsDatabase
from django.core.validators import URLValidator

# Create your views here.
def home(request):
    context={
        'get' : True
    }
    my_form = UrlForm()
    if request.method == 'POST':

        my_form = UrlForm(request.POST)
        cur_url = my_form.data['url']

        if(("http://" not in cur_url) and ("https://" not in cur_url)):
            cur_url = "http://"+cur_url

        url_validator = URLValidator()
        
        try :
            url_validator(cur_url)

            if UrlsDatabase.objects.filter(url=cur_url).exists():
                short_url = UrlsDatabase.objects.get(url=cur_url).uuid
                context={
                    'url' : cur_url,
                    'short_url' : "http://127.0.0.1:8000/"+short_url,
                }
            elif my_form.is_valid():
                new_url = my_form.cleaned_data['url']
                if(("http://" not in new_url) and ("https://" not in new_url)):
                    new_url = "http://"+new_url
                uid = str(uuid.uuid4())[:7]
                add_url = UrlsDatabase(url=new_url, uuid=uid)
                add_url.save()
                context={
                    'url' : new_url,
                    'short_url' : "127.0.0.1:8000/"+uid,
                }

        except ValidationError:
            context={
                'url' : None,
                'short_url' : None
            }

    return render(request, 'home.html', context=context)



def direct_url(request, uid):
    url_data = UrlsDatabase.objects.get(uuid=uid)
    return redirect(url_data.url)


