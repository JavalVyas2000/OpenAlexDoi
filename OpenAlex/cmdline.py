"""
This is the commandline prompt
"""
import click
from .works import Works

@click.command()
@click.argument("doi")
@click.option(
    "--format",
    default="bibtex",
    type=click.Choice(["bibtex", "ris"]),
    help="Output format (default: bibtex)",
)
def citation(doi, format):
    """
    Outputs RIS or Bibtex format for a given Doi string.
    """
    work = Works(doi)
    if format == "ris":
        print(work.ris())
    elif format == "bibtex":
        print(work.bibtex())
