# -*- coding: utf-8 -*-

import magic

from django import forms


class ParserForm(forms.Form):
    file = forms.FileField(label=u'Прикрепите CSV-файл')

    def clean(self, *args, **kwargs):
        attach_file = self.cleaned_data.get('file', '')
        if attach_file:
            if attach_file.content_type in ['text/csv', 'application/octet-stream']:
                with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
                    mime_type = m.id_buffer(attach_file.read())
                    attach_file.seek(0)
                if mime_type not in ['text/plain', 'application/x-empty']:
                    raise forms.ValidationError(u'Для загрузки доступны только CSV-файлы')
            else:
                raise forms.ValidationError(u'Для загрузки доступны только CSV-файлы')
