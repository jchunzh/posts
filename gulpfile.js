var gulp = require('gulp');
var sass = require('gulp-sass');
var runSequence = require('run-sequence');
var del = require('del');
var watch = require('gulp-watch');

var localDeploymentFolder = 'static/posts/';

gulp.task('default', function(callback) {
	runSequence('clean:static', ['sass', 'lib', 'js', 'img', 'html'], callback);
});

gulp.task('dev', function(callback) {
	runSequence('clean:static', ['sass', 'lib', 'js', 'img', 'html', 'watch'], callback);
});

gulp.task('watch', ['clean:static'], function() {
	gulp.watch('web/css/*.scss', ['sass']);
	gulp.watch('web/js/lib/**', ['lib']);
	gulp.watch(['web/js/**/*.js', '!web/js/!lib/', '!web/js/!tests/'], ['js']);
	gulp.watch('web/img/**', ['img']);
	gulp.watch('web/html/**', ['html']);
})

gulp.task('sass', function() {
	return gulp.src('web/css/*.scss')
	.pipe(sass())
	.on('error', function(error) {
		console.log(error.toString());

  		this.emit('end');
	})
	.pipe(gulp.dest(localDeploymentFolder + 'css'));
});

gulp.task('lib', function() {
	return gulp.src('web/js/lib/**/*.js')
	.pipe(gulp.dest(localDeploymentFolder + 'js/lib'));
});

gulp.task('js', function() {
	return gulp.src(['web/js/**/*.js', '!web/js/lib/**', '!web/js/tests/**', ])
	.pipe(gulp.dest(localDeploymentFolder + 'js'));
});

gulp.task('img', function() {
	return gulp.src('web/img/**')
	.pipe(gulp.dest(localDeploymentFolder + 'img'));
});

gulp.task('html', function() {
	return gulp.src('web/html/**')
	.pipe(gulp.dest(localDeploymentFolder + 'html'));
})

gulp.task('clean:static', function() {
	return del.sync(localDeploymentFolder);
});