from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from board.models import Post


def postlist(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def addpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


def postdetail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post_detail': post_detail})


def postmodify(request, post_id):
    post_modify = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post_modify)
        if form.is_valid():
            post_modify = form.save(commit=False)
            post_modify.save()
            return redirect('post_detail', post_id=post_modify.pk)
    else:
        form = PostForm(instance=post_modify)
    return render(request, 'post_modify.html', {'form': form})


def postdelete(request, post_id):
    post_delete = get_object_or_404(Post, pk=post_id)
    post_delete.delete()
    return redirect('post_list')

