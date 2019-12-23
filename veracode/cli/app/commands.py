import click
import sys
from veracode.application import Application
from veracode.sandbox import Sandbox

@click.group()
def app():
    pass


@app.command()
def list():
    for app in Application.list():
        click.echo(app)


@app.command()
@click.option('--name', '-n', required=True)
@click.option('--criticality', '-c', required=True, type=click.Choice(
    [ 'Very High', 'High', 'Medium', 'Low', 'Very Low' ]))

@click.option('--sandbox', '-s')
def create(name, criticality, sandbox=None):
    app = Application()
    app.name = name
    app.business_criticality = criticality
    app = app.save()
    if sandbox:
        sbx = Sandbox()
        sbx.name = sandbox
        app.sandbox = sbx


@app.command()
@click.option('--name', '-n', required=True,
        help='Name of application to update')
@click.confirmation_option('--force', '-f',
        help='Suppress prompt before removal.',
        prompt='Are you sure you want to delete this application')
def delete(name):
    app = Application(name)
    return app.delete()


@app.command()
@click.option('--name', '-n', required=True,
        help='Name of application to update.')
@click.option('--rename', '-r',
        help='New name for the application.')
@click.option('--criticality', '-c', type=click.Choice(
        [ 'Very High', 'High', 'Medium', 'Low', 'Very Low' ],
        case_sensitive=True), # update app to snake case so we can go -i
        help='New criticality for the application.')

def update(name, rename=None, criticality=None):
    # this isn't the right way to do this, google more
    if not (rename or criticality):
        with click.Context(update) as ctx:
            click.echo(update.get_help(ctx))
        sys.exit(('\nError: You must supply either "--rename / -r" '
                  'or "--criticality / -c"'))
    app = Application(name)
    app.name = rename
    app.business_criticality = '{}'.format(criticality)
    app.save()


@app.command()
def scan():
    click.echo('scan')

