import click
import time
from veracode.application  import Application
from veracode.sandbox  import Sandbox

@click.group()
def cli():
    pass

@cli.command()
@click.option('--app')
@click.option('--name')
@click.option('--files')
@click.option('--sandbox')
def scan(app, name, files, sandbox=None):
    app = Application(app)

    if sandbox:
        pass

    app.build.upload([files])
    app.build.scan()

    # status =''
    #
    # while

main = click.CommandCollection(sources=[cli])

if __name__ == '__main__':
    main()

