Fork
====

Fork is a Python package for making writing subprocesses easy.


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
