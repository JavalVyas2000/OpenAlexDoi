"""
This is the setup file and has the config details for the package.
"""
from setuptools import setup

setup(name='openalex',
      version='0.0.1',
      description='bibtex and ris from Doi',
      maintainer='Javal Vyas',
      maintainer_email='jvyas@andrew.cmu.edu',
      license='MIT',
      packages=['OpenAlex'],
      setup_requires=["nose>=1.0"],
      install_requires=["bibtexparser","IPython"],
      entry_points={
        "console_scripts": ["cite = openalex.cmdline:cite"]},
      long_description='''to get citations bibtex/ris''')
