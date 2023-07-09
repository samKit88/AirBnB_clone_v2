#!/usr/bin/python3
"""the `1-pack_web_static` module
defines the function `do_pack`
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """generates a .tgz archive from the contents of `web_static`"""
    formatted_time = datetime.now().strftime("%y%m%d%H%M%S")

    if not os.path.isdir("versions"):
        os.makedirs("versions")

    result = local("tar -cvzf versions/web_static_{}.tgz web_static".
                   format(formatted_time))
    if result.failed:
        return None
    else:
        local("chmod g+w versions/web_static_{}.tgz web_static".
              format(formatted_time))
        return "versions/web_static_{}.tgz".format(formatted_time)
