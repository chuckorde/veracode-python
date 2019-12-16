import click
import time
from veracode.application  import Application
from veracode.sandbox import Sandbox
from veracode.build import Build

@click.group()
def cli():
    pass

@cli.command()
@click.option('--app')
@click.option('--name')
@click.option('--files')
@click.option('--sandbox')
@click.option('--timeout')
def scan(app, name, files, sandbox=None, timeout=None):
    app = Application(app)
    
    app.sandbox = sandbox
    app.build = None
    b = Build()
    b.version = name
    app.build = b

    app.build.upload([files])
    app.build.scan()

    if timeout:
        timeout = int(timeout)
        for w in range(timeout):
            time.sleep(60)
            print('Scan status: {}'.format(app.build.analysis.status))

            if app.build.analysis.status == 'Results Ready':
                print('Veracode Security Policy: {}'.format(
                        app.build.policy.compliance))
                return app.build.policy.compliance == 'Pass'

        print('Scan timeout after {} minutes'.format(timeout))
        return 1

main = click.CommandCollection(sources=[cli])

if __name__ == '__main__':
    main()

