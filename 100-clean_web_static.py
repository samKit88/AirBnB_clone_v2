#!/usr/bin/python3
"""the `100-clean_web_static` module
defines the function `do_clean`
"""
from fabric.api import run, local, env

env.hosts = ["ubuntu@18.208.143.155", "ubuntu@3.226.255.224"]


def do_clean(number=0):
    """cleans old archives(deploys)"""
    num = int(number)
    if (num == 1 or num == 0):
        local('cd versions; ls -t | head -n -1 | xargs rm -rf')
        run('cd /data/web_static/releases; ls -t | head -n -1 | xargs rm -rf')
    else:
        local('cd versions; ls -t | head -n -{} | xargs rm -rf'.format(num))
        run('cd /data/web_static/releases; ls -t | head -n -{} | xargs rm -rf'.
            format(num))
