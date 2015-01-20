# try using distribute or setuptools or distutils.
try:
    import distribute_setup
    distribute_setup.use_setuptools()
except ImportError:
    pass

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import sys
import re

# parse version from package/module without importing or evaluating the code
with open('pycazy/pycazy.py') as fh:
    for line in fh:
        m = re.search(r"^__version__ = '(?P<version>[^']+)'$", line)
        if m:
            version = m.group('version')
            break

if sys.version_info <= (2, 5):
    sys.stderr.write("ERROR: pycazy requires Python Version 2.6 " +
                     "or above...exiting.\n")
    sys.exit(1)

setup(
    name="pycazy",
    version=version,
    author="Leighton Pritchard",
    author_email="leighton.pritchard@hutton.ac.uk",
    description=''.join(["pycazy provides programmatic access to the " +
                         "CAZy database at http://www.cazy.org/"]),
    license="GPLv3",
    keywords="CAZy bioinformatics enzymes database web",
    platforms="Posix; MacOS X",
    url="https://github.com/widdowquinn/pycazy",  # project home page
    download_url="https://github.com/widdowquinn/pycazy/releases",
    scripts=[],
    packages=['pycazy'],
#    install_requires=['networkx>=1.8.1'],
#    test_suite='tests.test_search.TestSearch',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
    )
