from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, ListView

from review.forms import PostForm
from review.models import Post


# def reviews(request):
#     posts = Post.objects.all()
#     return render(request, 'post_form.html', {'posts':posts})

# def postcreate(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = PostForm()
#     return render(request, 'post_form.html', {'form':form})


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'movie_name']

    template_name = 'review/post_form.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user

        if current_user.is_authenticated and (current_user.is_superuser or current_user.is_staff):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/reviews')

class PostList(ListView):
    model = Post
    ordering = '-timestamp'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = Post.object.all()

        return context
