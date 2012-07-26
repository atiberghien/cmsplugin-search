from setuptools import setup, find_packages

setup(
    name='cmsplugin-search',
    version='0.1',
    description='Search form plugin (and utils) for Django CMS Search app',
    author='Alban Tiberghien',
    author_email='alban.tiberghien@gmail.com',
    url='http://github.com/atibergien/cmsplugin-search',
    packages=find_packages(),
    install_requires=[
        'django-cms-search',
    ],
    keywords='search form django cms django-cms haystack plugin',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)