from setuptools import setup, find_packages
import os

setup(name='collective.easyslideshow',
      version=open(os.path.join("src", "collective", "easyslideshow", "version.txt")).read().strip(),
      description="An easy slideshow solution for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
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
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      paster_plugins = ["ZopeSkel"],
      setup_requires=["PasteScript"]
      )
