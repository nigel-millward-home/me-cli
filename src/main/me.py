import click

from files.files_cli import files


@click.group()
def entry_point():
    pass


entry_point.add_command(files)
