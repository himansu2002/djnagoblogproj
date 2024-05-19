from django.shortcuts import render
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin 


def index(request):
     posts = Post.objects.all()
     return render(request, 'blog/home.html', {'posts': posts})

# def home(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

class postListView(LoginRequiredMixin,ListView):
    model = Post
    template_name='blog/home.html'
    context_object_name ='posts'
    ordering = ['-date_posted']

class postDetailView(LoginRequiredMixin,DetailView):
    model = Post

class postCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['author','title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class postUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    
    model = Post
    fields = ['author','title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class postDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
    
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
   


