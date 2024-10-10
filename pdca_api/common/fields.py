# -*- coding: utf-8 -*-
import uuid
from django.core import exceptions
from django.db import models
from django.db.models import CharField, ForeignKey, UUIDField
from django.conf import settings
from django.utils.translation import gettext_lazy as _

__all__ = ('RemoteIdField', 'FileIdField', 'SimpleForeignKey')


class RemoteIdField(CharField):
    max_length = 64
    description = _("RemoteId (up to %(max_length)s)")

    def __init__(self, **kwargs):
        kw = kwargs.copy()
        kw['max_length'] = RemoteIdField.max_length
        kw['default'] = ''
        kw['blank'] = True
        kw['null'] = False
        super(RemoteIdField, self).__init__(**kw)


class FileIdField(CharField):
    max_length = 255
    description = _("RemoteId (up to %(max_length)s)")

    def __init__(self, **kwargs):
        kw = kwargs.copy()
        self.file_url_key = kw.pop('file_url_key', None)
        self.file_url_host = kw.pop('file_url_host', None) or settings.FILE_CDN_DOMAIN
        kw['max_length'] = kw.pop('max_length', None) or self.__class__.max_length
        kw['default'] = ''
        kw['blank'] = True
        kw['null'] = False
        super().__init__(**kw)


class SimpleForeignKey(ForeignKey):
    """
    默认外键字段, 没有外键约束, 有外键索引
    """
    on_delete = models.DO_NOTHING
    db_constraint = False

    def __init__(self, to, **kwargs):
        _cls = self.__class__
        kw = kwargs.copy()
        kw['on_delete'] = _cls.on_delete
        kw['db_constraint'] = _cls.db_constraint
        super().__init__(to, **kw)


class SimpleUUIDField(UUIDField):
    def __init__(self, verbose_name=None, **kwargs):
        kwargs['max_length'] = 32
        super().__init__(verbose_name, **kwargs)

    def to_python(self, value):
        if value is None:
            return None
        if value is not None and not isinstance(value, uuid.UUID):
            input_form = 'int' if isinstance(value, int) else 'hex'
            try:
                return str(uuid.UUID(**{input_form: value}))
            except (AttributeError, ValueError):
                raise exceptions.ValidationError(
                    self.error_messages['invalid'],
                    code='invalid',
                    params={'value': value},
                )
        return str(value)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        value = self.to_python(value)
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            return None
        if not isinstance(value, uuid.UUID):
            value = self.to_python(value)
            # value = uuid.UUID(value)
        if connection.features.has_native_uuid_field:
            return value
        return value.hex
