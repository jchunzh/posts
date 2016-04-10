from posts.models import Post
from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from django.shortcuts import render
from posts.Facades.PostFacade import PostFacade
from posts.Serializers.PostSerializer import PostSerializer
from django.shortcuts import render_to_response

import markdown

# def detail(request, post_id):
# 	post = get_object_or_404(Post, pk=post_id)
# 	return render(request, 'posts/detail.html', { 'post' : markdown_text(post) })

class PostsViewSet(viewsets.ViewSet):
	def __init__(self):
		self._postFacade = PostFacade()
		
	@list_route(methods=['get'])
	def getAllPublishedPosts(self, request):
		publishedPosts = self._postFacade.getAllPublishedPosts()
		serializedPosts = PostSerializer(publishedPosts, many=True)
		
		return Response(serializedPosts.data)
		
	