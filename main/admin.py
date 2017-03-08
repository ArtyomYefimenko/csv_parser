# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls import url

from .views import ParseDataView
from .models import Region, Country, ParserData


class ParseDataAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_data.html'
    list_display = ['group', 'country', 'value']
    search_fields = ['group__title', 'country__title', 'value']

    def get_urls(self):
        urls = super(ParseDataAdmin, self).get_urls()
        my_urls = [
            url(r'^parse_data/$', ParseDataView.as_view(), name='parse_data'),
        ]
        return my_urls + urls

admin.site.register(ParserData, ParseDataAdmin)
admin.site.register(Region)
admin.site.register(Country)

