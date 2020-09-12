from django.contrib import admin
from django.urls import path, re_path

from shortener.views import HomeView, URLRedirectView
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', HomeView.as_view()),
    re_path(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name = 'scode'),
]
