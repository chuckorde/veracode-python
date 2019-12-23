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
    app.build = name

    app.build.upload([files])
    app.build.scan()

    if timeout:
        timeout = int(timeout)
        for w in range(timeout):
            time.sleep(60)
            if app.build.analysis.status == 'Results Ready':
                print('Veracode Security Policy: {}'.format(
                        app.build.report.policy_rules_status))
                return 'Pass' in app.build.report.policy_rules_status
            app = Application(app.name, sandbox=sandbox, build=name)
            print('Scan status: {}'.format(app.build.analysis.status))
        print('Scan timeout after {} minutes'.format(timeout))
        return False

main = click.CommandCollection(sources=[cli])

if __name__ == '__main__':
    main()

