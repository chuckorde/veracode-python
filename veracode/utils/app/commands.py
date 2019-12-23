import click
import sys
import time
from veracode.application import Application
from veracode.sandbox import Sandbox
from veracode.build import Build
from veracode.utils.report import display

@click.group()
def app():
    pass


@app.command()
@click.option('--format', '-f',
        help='Output format.')
def list(format='simple'):
    headers = ['App ID', 'App Name']
    data = Application.list(name_only=False)
    display(data=data, headers=headers, format=format)


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
@click.option('--app', '-a', required=True,
        help='Name of the application.')
@click.option('--files', '-f', required=True,
        help='Files to upload.')
@click.option('--name', '-n',
        help='Name of the new scan.')
@click.option('--sandbox', '-s',
        help='Name of the sandbox.')
@click.option('--timeout', '-t', type=int,
        help='Timeout in minutes for scan results.')
def scan(app, files, name=None, sandbox=None, timeout=None):
    app = Application(app)
    app.sandbox = sandbox
    build = Build()
    build.name = name
    app.build = build
    app.build.upload([files])
    app.build.scan()

    if timeout:
        for w in range(timeout):
            time.sleep(60)
            if app.build.analysis.status == 'Results Ready':
                click.echo('Veracode Security Policy: {}'.format(
                        app.build.report.policy_rules_status))
                return 'Pass' in app.build.report.policy_rules_status
            app = Application(app.name, sandbox=sandbox, build=name)
            click.echo('Scan status: {}'.format(app.build.analysis.status))
        click.echo('Scan timeout after {} minutes'.format(timeout))
        return False


