# -*- coding: utf-8 -*-
"""
    fork
    ~~~~

    Doing subprocess in Python should be easy.

    :copyright: (c) 2014 by Shipeng Feng.
    :license: BSD, see LICENSE for more details.
"""
import sys
import shlex
import subprocess


PY2 = sys.version_info[0] == 2
if not PY2:
    text_type = str
    string_types = (str,)
    integer_types = (int,)
else:
    text_type = unicode
    string_types = (str, unicode)
    integer_types = (int, long)


def call(command, *args, **kwargs):
    """Monkey patching call.
    """
    if isinstance(command, string_types):
        command = shlex.split(command)
    return subprocess.call(command, *args, **kwargs)


class Popen(subprocess.Popen):
    """Monkey patching Popen.
    """

    def __init__(self, command, *args, **kwargs):
        if isinstance(command, string_types):
            command = shlex.split(command)
        super(Popen, self).__init__(command, *args, **kwargs)
