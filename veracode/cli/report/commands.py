import click

@click.group()
def report():
    pass

@report.command()
def list():
    click.echo('list')

@report.command()
def create():
    click.echo('create')

@report.command()
def delete():
    click.echo('delete')

@report.command()
def update():
    click.echo('update')

