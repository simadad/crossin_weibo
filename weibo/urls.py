from django.conf.urls import url
from weibo import views


urlpatterns = [
    url(r'^$', views.root, name='root')
]
