# -*- coding: utf-8 -*-

from django.db import models


class AbstractModel(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name=u'Название')

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        abstract = True


class Region(AbstractModel):

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'


class Country(AbstractModel):

    class Meta:
        verbose_name = u'Страна'
        verbose_name_plural = u'Страны'


class ParserData(models.Model):
    group = models.ForeignKey(Region, verbose_name=u'Группа')
    country = models.ForeignKey(Country, verbose_name=u'Параметр')
    value = models.CharField(max_length=255, verbose_name=u'Значение')

    class Meta:
        verbose_name = u'Данные'
        verbose_name_plural = u'Данные'
