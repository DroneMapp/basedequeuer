try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.0.4'

with open('requirements/production.txt') as requirements_file:
    requires = [line.strip('\n') for line in requirements_file if bool(line.strip('\n'))]


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Base Dequeuer',
    version=version,
    description="Common library for all Dequeuer incarnations",
    long_description=readme,
    author='Cléber Zavadniak',
    author_email='cleberman@gmail.com',
    url='https://github.com/Dronemapp/basedequeuer',
    license=license,
    packages=['basedequeuer'],
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'basedequeuer': 'basedequeuer'},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='generic libraries',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
