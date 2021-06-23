# -*- coding: utf-8 -*-
import os
import six
import sys
import time
import traceback

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.backends import utils
from django.utils.datastructures import OrderedSet
from six import PY3

import datetime
import os

from django.conf import settings
from django.core.cache import cache


class Command(BaseCommand):
    help = 'a shell import all models'
    from django.apps import apps
    loaded_models = apps.get_models()

    imported_objects = {
            'datetime': datetime,
            'cache': cache,
            'settings': settings,
        }

    for model in loaded_models:
        imported_objects[model.__name__] = model

    def get_imported_objects(self, options):
        imported_objects = self.imported_objects
        return imported_objects

    def get_kernel(self, options):
        try:
            from IPython import release
            if release.version_info[0] < 2:
                print(self.style.ERROR(
                    "--kernel requires at least IPython version 2.0"))
                return
            from IPython import start_kernel
        except ImportError:
            return traceback.format_exc()

        def run_kernel():
            imported_objects = self.get_imported_objects(options)
            kwargs = dict(
                argv=[],
                user_ns=imported_objects,
            )
            start_kernel(**kwargs)
        return run_kernel

    def handle(self, *args, **options):
        shell = self.get_kernel(options)
        shell()
