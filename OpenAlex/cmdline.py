"""
This is the commandline prompt
"""
import click
from .works import Works

@click.command()
@click.argument("doi")
@click.option(
    "--citation_format",
    default="bibtex",
    type=click.Choice(["bibtex", "ris"]),
    help="Output format (default: bibtex)",
)
def citation(doi, citation_format):
    """
    Outputs RIS or Bibtex format for a given Doi string.
    """
    work = Works(doi)
    if citation_format == "ris":
        print(work.ris())
    elif citation_format == "bibtex":
        print(work.bibtex())
