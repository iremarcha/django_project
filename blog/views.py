from django.shortcuts import render
from .models import Post
#v10
from django.views.generic import (ListView, 
								  DetailView,
								  CreateView,
								  UpdateView,
								  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# v2
#def home(request):
#	return HttpResponse('<h1>Blog Home</h1>')

#def about(request):
#	return HttpResponse('<h1>About</h1>')

#v3
posts = [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'August 27, 2018'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'August 28, 2018'
	}
]


def home(request):
	context = {
		#'posts': posts
		'posts': Post.objects.all()
	}
	return render(request,'blog/home.html', context)

#v10
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


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

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request,'blog/about.html',{'title':'About'})