from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.decorators import login_required, user_passes_test (function-based-views er khetre)
from .models import Post, Comment
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

"""
def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)
"""

"""
def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/home.html', {'posts': posts})
"""

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    """ei line ti use kora hoy karon class based view use korle home template er
       for loop hobe "for post in object_list". ei line ti dile "for post in posts" use kora jabe.
       By default, ListView provide the context as object_list."""
    paginate_by = 8

    # Post Search korar jonno ei method.
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            posts = self.model.objects.filter(title__icontains=query)
        else:
            posts = self.model.objects.all()
            return posts



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
       context = super(PostDetailView, self).get_context_data(**kwargs)
       context['commentform'] = CommentForm()
       return context

    def post(self, request, slug):
       post = get_object_or_404(Post, slug=slug)
       form = CommentForm()

       if request.method == 'POST':
           form = CommentForm(request.POST)

           if form.is_valid():
               # Create "Comment object" but don't save to the database yet.
                comment  = form.save(commit=False)
                # Assign the current post to the comment.
                comment.post = post
                comment.name = self.request.user
                # Save the comment to the database
                comment.save()
                return redirect('blog:post-detail', slug=slug)

       else:
           form = commentform()



@login_required # ei decorator use korle settings e LOGIN_URL = 'login' setup kore dite hobe.
def CreatePost(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.slug = slugify(post.title)
        post.author = request.user
        post.save()
        messages.success(request, f'Congratulations! Your post has been created!')
        return redirect('blog:post-detail', slug=post.slug)

    else:
        form = PostForm()
        
    return render(request, 'blog/post_form.html',{'form':form})



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # You should return to home now. Because you have already deleted the post.

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def policies(request):
    return render(request, 'blog/policies.html', {'title': 'Policies'})


def features(request):
    return render(request, 'blog/features.html', {'title': 'Features'})

