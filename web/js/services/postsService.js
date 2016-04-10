app.factory('postsService', ['$resource', function ($resource) {
	var url = '/posts/api/posts/';

	return $resource(url, null, { 
		getAllPublishedPosts : { method : 'GET', url : url + 'getAllPublishedPosts', isArray : true }
	}, {
		stripTrailingSlashes : false
	});
}])