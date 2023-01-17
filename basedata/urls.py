from django.urls import re_path, include
import basedata.views

urlpatterns = [
    re_path(r"dataimport/(?P<object_id>\d+)/action", basedata.views.action_import),
]
