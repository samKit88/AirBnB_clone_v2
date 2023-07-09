#!/usr/bin/python3
"""the `2-do_depliy_web_static` module
defines the function `do_deploy`
"""
from fabric.api import run, put, env
from os import path

env.hosts = ["ubuntu@18.208.143.155", "ubuntu@3.226.255.224"]


def do_deploy(archive_path):
    """deploys the archived `web_static` on the servers"""

    if not path.exists(archive_path):
        return False
    else:
        try:
            last_index = archive_path.rfind("/") + 1
            archive_name = archive_path[last_index:]
            without_extension = archive_name[: archive_name.find(".")]
            put(archive_path, "/tmp/")
            run("mkdir -p /data/web_static/releases/{}/".
                format(without_extension))
            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                    archive_name, without_extension))
            run("mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(
                without_extension, without_extension))
            run("rm -rf /data/web_static/releases/{}/web_static".format(
                    without_extension, without_extension))
            run("rm -f /tmp/{}".format(archive_name))
            run("rm -f /data/web_static/current")
            run("ln -s /data/web_static/releases/{} /data/web_static/current".
                format(without_extension))
            return True
        except Exception:
            return False
