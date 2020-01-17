import click
from veracode.application import Application
from veracode.utils.report import display

@click.group(help='View application policy report(s).')
def report():
    pass

@report.command(help='Print policy summary.')
@click.option('--app', '-a', required=True,
        help='Name of the application.')
@click.option('--sandbox', '-s',
        help='Name of the application sandbox.')
@click.option('--build', '-b',
        help='Name of the application build.')
@click.option('--format', '-f', default='list',
        help='Output format.')
def summary(app, sandbox=None, build=None, format=None):
    app = Application(name=app, sandbox=sandbox, build=build)
    report = app.build.report
    headers = ['Policy Name',
	       'Policy Status',
	       'Score',
	       'Total Flaws',
	       'Very High',
	       'High',
	       'Medium',
	       'Low']
    data = [[
	report.policy_name,
	report.policy_compliance_status,
	report.static_analysis.score,
	report.flaw_status.total,
	report.flaw_status.sev_5_change,
	report.flaw_status.sev_4_change,
	report.flaw_status.sev_3_change,
	report.flaw_status.sev_2_change,
    ]]
    display(data=data, headers=headers, format=format)

@report.command()
def create():
    click.echo('create')

@report.command()
def delete():
    click.echo('delete')

@report.command()
def update():
    click.echo('update')

