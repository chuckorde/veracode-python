import click
from veracode.application import Application
from veracode.utils.report import display

@click.group()
def report():
    pass

@report.command()
@click.option('--app', '-a', required=True,
        help='Name of the application.')
@click.option('--sandbox', '-s',
        help='Name of the application sandbox.')
@click.option('--build', '-b',
        help='Name of the application build.')
def summary(app, sandbox=None, build=None):
    app = Application(name=app, sandbox=sandbox, build=build)
    print(app.build.report)

@report.command()
def create():
    click.echo('create')

@report.command()
def delete():
    click.echo('delete')

@report.command()
def update():
    click.echo('update')

