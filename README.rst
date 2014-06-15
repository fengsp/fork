Fork
====

Fork is a Python package for making writing subprocesses easy.  Currently
we just monkey patching the ``call`` and ``Popen`` so that they support
taking string like command.


Installation
------------

::
    
    $ pip install fork


Usage
-----

.. code:: python

    import fork

    # call
    fork.call('pip  install requests')
    fork.call('date')
    fork.call('touch /tmp/hello\ fork.txt')

    # Popen
    p = fork.Popen('ls -l', stdout=fork.subprocess.PIPE)
    output, error = p.communicate()
    print p.pid
    print output
    print p.returncode


Better
------

If you feel anything wrong, feedbacks or pull requests are welcomed.
