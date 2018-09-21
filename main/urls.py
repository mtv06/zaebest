from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexListView.as_view(), name='index'),
    url(r'^search/$', views.SearchListView.as_view(), name='search'),
    url(r'^added-places/$', views.AddedPlacesListView.as_view(), name='added_places'),
    url(r'^liked-places/$', views.LikedPlacesListView.as_view(), name='liked_places'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
]