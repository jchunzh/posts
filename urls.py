from django.conf.urls import url, include
from . import views
from rest_framework import routers
from django.views.generic import TemplateView

router = routers.SimpleRouter()
router.register(r'api/posts', views.PostsViewSet, 'Posts')

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='posts/index.html'), name='index'),
    url(r'^', include(router.urls))
]

for u in router.urls: 
	print(u)