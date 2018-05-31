from setuptools import setup

VERSION = "0.0.1-snapshot"
PACKAGE_NAME = "3.6webserver"
DEVELOPMENT_STATUS = ".001 - Gamma"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

EXTRAS = {}
REQUIRES = []
with open('requirements.txt') as f:
    for line in f:
        line, _, _ = line.partition('#')
        line = line.strip()
        if ';' in line:
            requirement, _, specifier = line.partition(';')
            for_specifier = EXTRAS.setdefault(':{}'.format(specifier), [])
            for_specifier.append(requirement)
        else:
            REQUIRES.append(line)
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description="python 3.6 API/Web server",
    author_email="",
    author="r.lawhorn",
    license="Apache License Version 2.0",
    url="https://github.com/",
    install_requires=REQUIRES,
    packages=[],
    include_package_data=True,
    ],
)
