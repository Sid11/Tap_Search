from django.shortcuts import render, HttpResponse , redirect
from tap.document import PostDocument , ImageForm
from elasticsearch import Elasticsearch
from .models import Post,Image
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# Create your views here.

def home(request):
    #return HttpResponse("The World Makes Sense")
    return render(request,'home.html',{})

def add(request):
    a = request.POST.get('search')
    print("1")
    if a:
        p = Post(para=a)
        p.save()
        print("Value of a ", str(a))
        return HttpResponse("Para is " + str(a))
    else:
        return HttpResponse("Please fill in some data")


def search(request):

    q = request.GET.get('q')

    if q:
        posts = PostDocument.search().query("match", para=q)
    else:
        posts = ''

    return render(request, 'search.html', {'posts': posts})






def image(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = ImageForm()
    return render(request, 'image.html', {'form': form})



