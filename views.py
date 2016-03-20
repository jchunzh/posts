from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown

def index(request):
	posts = Post.objects.filter(is_published=True).order_by('-published_date')

	for p in posts:
		markdown_text(p)

	return render(request, 'posts/index.html', { 'posts' : posts})

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'posts/detail.html', { 'post' : markdown_text(post) })

def markdown_tutorial(request):
	return render(request, 'posts/markdown.html')

def markdown_text(post):
	post.text = markdown.markdown(post.text)