import click


@click.group(help='files_utilities')
def files():
    pass


@files.command(help='Delete files from your downloads directory')
@click.option('--days', default=7, show_default=True, help='Delete files > days')
def delete_downloads(days):
    from files.files import delete_downloads
    delete_downloads(days)
