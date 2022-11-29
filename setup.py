from setuptools import setup, find_packages
import os

tests_require = [
    "zope.testing",
    "collective.testcaselayer",
]

version = open(os.path.join(
    "src",
    "collective",
    "easyslideshow",
    "version.txt")).read().strip()

readme_text = open(os.path.join(
    "src",
    "collective",
    "easyslideshow",
    "README.txt")).read()

setup(name='collective.easyslideshow',
      version=version,
      description="An easy slideshow solution for Plone",
      long_description=readme_text + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from:
      # http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        ],
      keywords='plone slideshow',
      author='Six Feet Up, Inc.',
      author_email='info@sixfeetup.com',
      url='http://svn.plone.org/svn/collective/collective.easyslideshow',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'zope.formlib',
      ],
      tests_require=tests_require,
      extras_require={'tests': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
