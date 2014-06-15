# -*- coding: utf-8 -*-
"""
    hello-fork
    ~~~~~~~~~~

    Examples for fork.

    :copyright: (c) 2014 by Shipeng Feng.
    :license: BSD, see LICENSE for more details.
"""
import fork


def call():
    """Demo call."""
    fork.call('pip  install requests')
    fork.call('date')
    fork.call('touch /tmp/hello\ fork.txt')


def popen():
    """Demo Popen."""
    p = fork.Popen('ls -l', stdout=fork.subprocess.PIPE)
    output, error = p.communicate()
    print p.pid
    print output
    print p.returncode


def run():
    """Demo all."""
    call()
    popen()


if __name__ == "__main__":
    run()
