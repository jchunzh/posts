from posts.Repositories.PostRepository import PostRepository
from datetime import datetime

class PostFacade():
	def __init__(self):
		self._postRepository = PostRepository();

	def getAllPublishedPosts(self):
		posts = self._postRepository.getAllPublishedPosts();

		for p in posts:
			p.formated_published_date = p.published_date.strftime("%B %d, %Y")

		return posts