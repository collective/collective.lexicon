from setuptools import setup, find_packages
import os

version = '1.0'

setup(
    name='collective.lexicon',
    version=version,
    description="A better way to manage vocabulary",
    long_description=open("README.rst").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.rst")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Andy Leeb, Clayton Parker, Nathan VanGheem, John Olson',
    author_email='ableeb@andyleeb.com',
    url='http://svn.plone.org/svn/collective/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    extras_require={'tests': ['plone.app.testing']},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
