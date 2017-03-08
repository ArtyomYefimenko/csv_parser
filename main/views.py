# -*- coding: utf-8 -*-

import csv
import json

from django.contrib import messages
from django.db import transaction
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.views.generic import FormView, TemplateView


from .forms import ParserForm
from .models import Region, Country, ParserData


class ParseDataView(FormView):
    form_class = ParserForm
    template_name = 'admin/data_result_list.html'
    messages = {
        'incorrect_coding': u"Некорректная кодировка файла. Файл должен быть в кодировке UTF-8",
    }

    @staticmethod
    def check_coding(request_file):
        try:
            request_file.read().decode('utf-8')
            request_file.seek(0)
            return True
        except UnicodeDecodeError:
            return False

    @transaction.atomic
    def form_valid(self, form, **kwargs):
        data = self.request.FILES['file']
        if not self.check_coding(data.file):
            messages.error(self.request, self.messages['incorrect_coding'])
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

        lines = filter(None, map(lambda line: line.strip(), data))
        if len(lines) == 0:
            messages.error(self.request, u"Файл пуст. Загрузите другой файл")
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

        csvreader = list(csv.reader(data, delimiter=','))
        already_exists = 0
        ok = 0

        for row in csvreader[1:]:
            if len(row) != 3:
                continue

            try:
                region_title = row[0].strip()
                country_title = row[1].strip()
                value = row[2].strip()
            except IndexError:
                continue

            region, created = Region.objects.get_or_create(title=region_title)
            country, created = Country.objects.get_or_create(title=country_title)
            if ParserData.objects.filter(group_id=region.id, country_id=country.id, value=value).exists():
                already_exists += 1
                continue
            ParserData.objects.create(group_id=region.id, country_id=country.id, value=value)
            ok += 1

        if ok > 0:
            messages.success(self.request, u"Создано данных: {} шт.".format(ok))
        elif already_exists > 0:
            messages.warning(self.request, u"Данные уже в базе")
        else:
            messages.error(self.request, u"Данные не созданы!")
        return HttpResponseRedirect(reverse_lazy('admin:main_parserdata_changelist'))


class HomeView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        ctx = []
        for reg in Region.objects.all():
            s = {
                'name': reg.title,
                'value': json.dumps([{'country__title': ''}] +
                                    list(reg.parserdata_set.values('country__title', 'value')) +
                                    [{'country__title': ''}])
            }
            ctx.append(s)
        context.update({'groups': ctx})
        return context
