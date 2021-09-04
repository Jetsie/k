from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import content.views


urlpatterns = [
    path("", content.views.index, name="index"),
    path("db/", content.views.db, name="db"),
    path("admin/", admin.site.urls),
]
