from django.shortcuts import render

from board.models import Post


def postlist(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts':posts})



