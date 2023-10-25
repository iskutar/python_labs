#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#TEST

#ON_NEW_BRANCH

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


if __name__ == '__main__':
    main()
