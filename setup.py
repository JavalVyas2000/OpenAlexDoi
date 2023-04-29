"""
This is the setup file and has the config details for the package.
"""
from setuptools import setup

setup(name='OpenAlex_Doi',
      version='0.0.1',
      description='bibtex and ris from Doi',
      maintainer='Javal Vyas',
      maintainer_email='jvyas@andrew.cmu.edu',
      license='MIT',
      packages=['OpenAlex'],
      setup_requires=["IPython"],
      install_requires=["bibtexparser","IPython"],
      entry_points={
        "console_scripts": ["citation = OpenAlex_Doi.cmdline:citation"]},
      long_description='''to get citations in bibtex or ris format''')
