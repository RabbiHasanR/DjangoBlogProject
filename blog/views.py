from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from blog.models import Post,Comment
from blog.forms import PostForms,CommentForms
from django.utils import timezone

# Create your views here.
class AboutView(TemplateView):
    template_name='about.html'

class PostListView(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model=Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=PostForms
    model=Post
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=PostForms
    model=Post

class PostDeleteView(LoginRequiredMixin,DeleteView): 
    model=Post
    success_url=reverse_lazy('blog:post_list')

class DraftPostView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='blog/post_list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')




#######################################
#######################################
@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=post.pk)

@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentForms(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form=CommentForms()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def commnet_approve(request,pk):
    comment=get_object_or_404(Comment, pk=pk)
    comment.approved()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def commnet_remove(request,pk):
    comment=get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:post_detail',pk=comment.post.pk)
