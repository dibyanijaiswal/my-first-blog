from django.shortcuts import render

def postlist(request):
    return render(request,'blog/postlist.html',{})

# Create your views here.
