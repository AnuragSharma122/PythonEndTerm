from django.db import connection
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from .models import Comment, Post
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView,DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .forms import CommentForm

# Create your views here.

def home(request):
    
    if request.method == 'POST':
        first_name = User.first_name  
        last_name = User.last_name
        username = User.username
        content = request.POST['content'] 
        image = request.FILES.get('image')

        if content:
            posts = Post(content = content, image = image,author =request.user)
            posts.save()
            return redirect('/')
        else:
            messages.info(request, 'Please input')
            return redirect('/')
    else:
        context = {
        'posts': Post.objects.all().order_by('-id')
        }
        return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

# def addComment(request):
#     if request.method == 'POST':
#         comment = request.POST['comment']
#         post = Post

#         if comment:
#             comments = Comment(body = comment, author = request.user, name = Post.content)
#             comments.save()
#             return redirect('/')
#         else:
#             messages.info(request, 'Please input')
#             return redirect('/')


class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked

        def post(self , request, *args, **kwargs):
            form = CommentForm(request.POST)
            if form.is_valid():
                post = self.get_object()
                form.instance.user = request.user
                form.instance.post = post
                form.save()

                return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))
        return data
    


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content', 'image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def likePostApp(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('like'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

