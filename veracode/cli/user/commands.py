import click

@click.group()
def user():
    pass

@user.command()
def list():
    click.echo('list')

@user.command()
def create():
    click.echo('create')

@user.command()
def delete():
    click.echo('delete')

@user.command()
def update():
    click.echo('update')

