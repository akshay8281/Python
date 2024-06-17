from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def index(request):
	return render(request,'index.html')


def make_post(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        author = request.POST["author"]
        created_at = request.POST["created_at"]
        new_post = Post(title=title, content=content, author=author, created_at=created_at)
        new_post.save()

        return render(request, 'success.html', {'post': new_post})
    else:
        return render(request, 'make_post.html')
