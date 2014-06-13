"""
Fork
----

A simple wrapper around subprocess for easy subprocess calling.

Links
`````

* `development version
  <http://github.com/fengsp/fork/zipball/master#egg=fork-dev>`_

"""
from setuptools import setup


setup(
    name='fork',
    version='0.1',
    url='https://github.com/fengsp/fork',
    license='BSD',
    author='Shipeng Feng',
    author_email='fsp261@gmail.com',
    description='A Python package for doing subprocess easily.',
    long_description=__doc__,
    py_modules=['fork'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)
