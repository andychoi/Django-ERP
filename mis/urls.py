from django.urls import path
from django.urls import include, re_path
from django.conf.urls import static
from django.contrib import admin
from mis import settings
import workflow.views
import invent.urls
import basedata.urls
import selfhelp.urls
import mis.views


admin.site.site_header = 'Django-ERP'
admin.site.site_title = 'ERP'

urlpatterns = [
    path('', mis.views.home),
    re_path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/start", workflow.views.start),
    re_path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/approve/(?P<operation>\d+)", workflow.views.approve),
    re_path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/restart/(?P<instance>\d+)", workflow.views.restart),
    re_path(r'^admin/', admin.site.urls, name="admin"),
    re_path(r'^admin/invent/', include(invent.urls)),
    re_path(r'^admin/basedata/', include(basedata.urls)),
    re_path(r'^admin/selfhelp/', include(selfhelp.urls)),
]
urlpatterns += static.static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static.static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
