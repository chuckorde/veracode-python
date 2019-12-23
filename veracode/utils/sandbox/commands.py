import click

@click.group()
def sandbox():
    pass

@sandbox.command()
def list():
    click.echo('list')

@sandbox.command()
def create():
    click.echo('create')

@sandbox.command()
def delete():
    click.echo('delete')

@sandbox.command()
def update():
    click.echo('update')

