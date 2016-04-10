from django.test import TestCase
from posts.models import Post
from posts.Repositories.PostRepository import PostRepository
from posts.Facades.PostFacade import PostFacade
from unittest.mock import MagicMock
from datetime import datetime

class testGetAllPublishedPosts(TestCase):
	def setUp(self):
		self.sut = PostFacade()

	def test_formats_published_date(self):
		persistedPosts = [
		Post(published_date=datetime(2016, 1, 1, hour=13, minute=1))
		]
		self.sut._postRepository.getAllPublishedPosts = MagicMock(return_value=persistedPosts)

		formatedPosts = self.sut.getAllPublishedPosts();

		self.assertEqual(formatedPosts[0].formated_published_date, "January 01, 2016")
		