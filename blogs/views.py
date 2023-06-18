from django.shortcuts import render
from .models import *

def blog_single(req, pid):
    try :
        post = Post.objects.get(id=pid, status=True)
        post.counted_views += 1
        post.save()
        context = {
            'post': post,
            }
        return render(req, 'blogs/Commodity Details.html', context=context)
    except:
        return render(req, 'blogs/404.html')


# Create your views here.
