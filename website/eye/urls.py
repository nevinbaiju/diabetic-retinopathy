from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^result', views.result, name = 'result'),
]