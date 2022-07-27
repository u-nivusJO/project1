from django.shortcuts import render, get_object_or_404
from .models import Post

def postlist(request):
    post_list=Post.objects.order_by('-post_num')
    context={'post_list':post_list}
    return render(request, 'boards/post_list.html', context)

def postpage(request, post_num):
    post=Post.objects.get_object_or_404(Post, pk=post_num)
    context={'post':post}
    return render(request, 'boards/post_page.html', context)