from django.test import TestCase
from posts.models import Post
from posts.Repositories.PostRepository import PostRepository
from django.utils import timezone

class testGetAllPublishedPosts(TestCase):
	def setUp(self):
		self.sut = PostRepository()
	
	def test_gets_only_published_posts(self):
		posts = [
			Post(text='first published', is_published=True, published_date=timezone.now()),
			Post(text='first draft', is_published=False, published_date=None),
			Post(text='second published', is_published=True, published_date=timezone.now()),
			Post(text='third published', is_published=True, published_date=timezone.now()),
			Post(text='fourth published', is_published=True, published_date=timezone.now()),
			Post(text='second draft', is_published=False, published_date=None)
		]
		
		self._savePosts(posts)
		
		result = self.sut.getAllPublishedPosts()
		
		self.assertEqual(len(result), 4)
		self.assertEqual(posts[0].id, result[0].id)
		self.assertEqual(posts[2].id, result[1].id)
		self.assertEqual(posts[3].id, result[2].id)
		self.assertEqual(posts[4].id, result[3].id)
		
	def _savePosts(self, posts):
		for p in posts:
			p.save()