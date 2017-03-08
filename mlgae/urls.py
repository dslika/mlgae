import session_csrf
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve

from mlgae import settings
from mlgae import views

session_csrf.monkeypatch()

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', views.home),
    url(r'^polls/', include('polls.urls')),
    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),
]

if settings.DEBUG:
    urlpatterns += tuple(static(settings.STATIC_URL, view=serve, show_indexes=True))
