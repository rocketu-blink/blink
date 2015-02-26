from django.conf.urls import url, include
from rest_framework import routers, filters
from blink_app import views
from blink_app.views import ContentViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'content', views.ContentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'results', views.SearchViewSet.as_view(),),
    url(r'^', include(router.urls)),

]