from django.urls import re_path, include
import selfhelp.views

urlpatterns = [
    re_path(r"(?P<model>\w+)/(?P<object_id>\d+)/pay", selfhelp.views.pay_action),
]
