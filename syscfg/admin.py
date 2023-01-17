# coding=utf-8
from django.contrib import admin
from django.forms import ModelForm,DateField
from syscfg.models import *
from common import generic


class SiteForm(ModelForm):
    """

    """
    class Meta:
        model = Site
        fields = '__all__'


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name', 'begin', 'end']
    fields = (('begin', 'end'), 'name', 'description', 'user')
    filter_horizontal = ['user']
    form = SiteForm


@admin.register(Module)
class ModuleAdmin(generic.BOAdmin):
    CODE_NUMBER_WIDTH = 3
    CODE_PREFIX = 'U'
    list_display = ['code','name','parent','status']
    ordering = ['weight']
    raw_id_fields = ['parent']


@admin.register(Menu)
class MenuAdmin(generic.BOAdmin):
    CODE_NUMBER_WIDTH = 3
    CODE_PREFIX = 'M'

    list_display = ['code','name','module','status']
    list_filter = ['module']
    ordering = ['weight']
    raw_id_fields = ['module']


@admin.register(Role)
class RoleAdmin(generic.BOAdmin):
    CODE_NUMBER_WIDTH = 3
    CODE_PREFIX = 'R'
    list_display = ['code','name','status']
    filter_horizontal = ['users','menus']


