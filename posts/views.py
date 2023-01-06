
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Postform
from .models import Post


# Create your views here.
def index(request):
    # If the method is POST
    if request.method == "POST":
        #if the form is valid
        form = Postform(request.POST,request.FILES)
        if form.is_valid():
            #Yes, save
            form.save()

            #Redirect to Home
            return HttpResponseRedirect('/')

        else:
            #No, show error
            return HttpResponseRedirect(form.erros.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all()
    #Show
    return render(request, 'posts.html', 
                    {'posts': posts})

def delete(request, post_id):
    # Find post 
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')
   
def edit(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = Postform(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.erros.as_json())   
    return render(request,'edit.html',{'post':post})            


def likes(request, post_id):
    count=Post.objects.get(id=post_id)
    count.count +=1
    count.save()
    # newlikecount = Post.objects.get(id=post_id)
    # newlikecount.likecount +=1 
    # newlikecount.save()
    return HttpResponseRedirect('/')

