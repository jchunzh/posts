from posts.models import Post

class PostRepository():
	def getAllPublishedPosts(self):
		return Post.objects.filter(is_published=True)