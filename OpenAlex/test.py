"""
This is the testing file
"""
from .works import Works

REF_BIBTEX = """author = John R. Kitchin,title = Examples of Effective Data Sharing in Scientific Publishing,\
volume = 5,number = , 6,pages = 3894-3899,year = 2015,doi = "https://doi.org/10.1021/acscatal.5b00538",\
url = "https://doi.org/10.1021/acscatal.5b00538",DATE_ADDED = 2023-04-25T07:12:46.013456"""


def test_bibtex():
 """
 The below function is implemented to test the bibtex
 """
 work = Works("https://doi.org/10.1021/acscatal.5b00538")
 assert REF_BIBTEX == work.bibtex(),'Error!!!'
 return 'Test Completed Successfully'

REF_RIS='''<pre>TY  - JOUR\nAU  - John R. Kitchin\nPY  - 2015\nTI  - Examples of Effective Data Sharing in Scientific Publishing\n\
JO  - ACS Catalysis\nVL  - 5\nIS  - 6\nSP  - 3894\nEP  - 3899\nDO  - https://doi.org/10.1021/acscatal.5b00538\n\
ER  -<pre><br><a href="data:text/plain;base64,VFkgIC0gSk9VUgpBVSAgLSBKb2huIFIuIEtpdGNoaW4KUFkgIC0gMjAxNQpUSSAgLSBFeGFtcGxlcyBvZiBFZmZlY3RpdmUgRGF0YSBTaGFyaW5nIGluIFNjaWVudGlmaWMgUHVibGlzaGluZwpKTyAgLSBBQ1MgQ2F0YWx5c2lzClZMICAtIDUKSVMgIC0gNgpTUCAgLSAzODk0CkVQICAtIDM4OTkKRE8gIC0gaHR0cHM6Ly9kb2kub3JnLzEwLjEwMjEvYWNzY2F0YWwuNWIwMDUzOApFUiAgLQ==" download="ris">Download RIS</a>'''

def test_ris():
 """
 The below function is implemented to test the ris
 """
 work = Works("https://doi.org/10.1021/acscatal.5b00538")
 assert REF_RIS == work.ris(),'Error!!!'
 return 'Test Completed Successfully'
