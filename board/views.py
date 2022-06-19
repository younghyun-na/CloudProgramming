from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from board.models import Post


def postlist(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def addpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list.html')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

def postdetail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post_detail': post_detail})

