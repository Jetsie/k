from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import content.views


urlpatterns = [
    path("", content.views.home, name="home"),
    path("db/", content.views.db, name="db"),
    path("admin/", admin.site.urls),
]
