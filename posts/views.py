from django.shortcuts import render
from .models import Post
from .forms  import PostForm
from django.shortcuts import get_object_or_404,redirect
# Create your views here.

def home(request):
    return render(request,'index.html')

def post_list(request):
    Post.objects.all().order_by('-created_at')
    return render(request,'post_list.html',{'posts':posts})
