#! /usr/bin/env python
__author__ = 'clh'
"""
The purpose of this script is to search through the config of all of your heroku apps,
and tell you which apps and config matched.
Relies on the heroku command line tool being installed, and logged in to your account
"""
import subprocess
import re
import sys

heroku_path = '/usr/local/bin/heroku'
app_name_re = re.compile('^([\w-]+)')


def get_app_names():
    output = subprocess.check_output([heroku_path, 'apps'])
    apps = []
    for token in output.split('\n'):
        # skip empty lines, and meta data lines.
        m = app_name_re.match(token)
        if m is not None:
            apps.append(m.group(1))
    return apps


def get_app_config(app_name):
    raw_output = subprocess.check_output([heroku_path, 'config', '--app', app_name])
    lines = raw_output.split('\n')
    config = [lines[0], lines[1:]]
    return config


def search_config(search_term, config):
    print config[0]
    for config_line in config[1]:
        m = re.search(search_term, config_line)
        if m is not None:
            print config_line
    print '\n'


def main(search_term):
    # first get all the apps
    apps = get_app_names()
    print "Searching config for {0} Heroku apps.".format(len(apps))
    for app in apps:
        config = get_app_config(app)
        search_config(search_term, config)
    return 0  # alls well


if __name__ == '__main__':
    search_term = sys.argv[1]
    if search_term is None:
        sys.exit(1)
    code = main(search_term)
    print 'Exiting:{0}'.format(code)
    sys.exit(code)