"""
This is the testing file
"""
import re
from .works import Works

REF_BIBTEX = """author = John R. Kitchin,\title = Examples of Effective Data Sharing in Scientific Publishing,\
volume = 5,number = , 6,pages = 3894-3899,year = 2015,doi = "https://doi.org/10.1021/acscatal.5b00538",\
url = "https://doi.org/10.1021/acscatal.5b00538",DATE_ADDED = 2023-04-25T07:12:46.013456"""


def test_bibtex():
 work = Works("https://doi.org/10.1021/acscatal.5b00538")
 assert REF_BIBTEX == work.bibtex()
