from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)


class HomePage(LoginRequiredMixin,TemplateView):
    template_name = 'backend/index.html'

class BlogListPage(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'backend/blog/list.html'

class BlogNewPage(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    form_class = PostForm
    template_name = 'backend/blog/new.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


#######################################
## Functions that require a pk match ##
#######################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('home')
