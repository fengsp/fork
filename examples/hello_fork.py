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


def run():
    """Demo all."""
    call()


if __name__ == "__main__":
    run()
