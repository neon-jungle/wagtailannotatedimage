#!/usr/bin/env python3

import os
import shutil
import sys


def run():
    from django.core.management import execute_from_command_line
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.app.settings'
    os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = "localhost:8000-8010,8080,9200-9300"
    try:
        execute_from_command_line([sys.argv[0], 'test'] + sys.argv[1:])
    finally:
        from tests.app.settings import STATIC_ROOT, MEDIA_ROOT
        shutil.rmtree(STATIC_ROOT, ignore_errors=True)
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)

if __name__ == '__main__':
    run()