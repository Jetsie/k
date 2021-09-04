from django.urls import path, include

from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

import content.views


urlpatterns = [
    path("", content.views.index, name="index.html"),
    path("index.html", content.views.index, name="index.html"),
    path("admin/", admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
