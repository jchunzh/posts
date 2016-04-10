app.controller('indexController', ['$scope', '$location', 'postsService', function($scope, $location, postsService) {
	$scope.posts = [];
	$scope.test = 'hello world';
	$scope.projects = getProjects($location);
	$scope.home = 'http://' + $location.host() + ':' + $location.port();

	postsService.getAllPublishedPosts([], function(value, responseHeaders) {
		$scope.posts = value;
	}, function(){});
}]);


function getProjects($location) {
	var projects = [
		{
			name: 'QuickPoll',
			url: "http://" + $location.host() + ':' + $location.port() + '/quickpoll'
		}
	];
	
	return projects;
}