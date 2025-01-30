#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.shortcuts import render
from ytmusicapi import YTMusic

ytmusic = YTMusic()

track_results = ytmusic.search("YOASOBI", filter="songs")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'searchMusic_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def mainpage(request):
    return render(request, 'template/account_system/main.html')

def login_page(request):
    return render(request, 'template/account_system/login.html')

if __name__ == '__main__':
    main()
