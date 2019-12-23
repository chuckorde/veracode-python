import click
from veracode.user import User
from veracode.utils.report import display

@click.group()
def user():
    pass

@user.command()
@click.option('--format', '-f',
        help='Output format.')
@click.option('--email', '-e',
        help="Search by user's email address.")
@click.option('--first-name', '-n',
        help="Search by user's first name.")
@click.option('--last-name', '-l',
        help="Search by user's last name.")
def list(email=None, first_name=None, last_name=None, format='simple'):
    headers = ['First Name', 'Last Name', 'Email', 'Last Login']
    data = User.list(name_only=False, email=email, first_name=first_name,
                     last_name=last_name)
    display(data=data, headers=headers, format=format)

@user.command()
@click.option('--email', '-e', required=True,
        help="The new user's email address.")
@click.option('--first-name', '-n', required=True,
        help="The new user's first name.")
@click.option('--last-name', '-l', required=True,
        help="The new user's last name.")
@click.option('--roles', '-r', required=True,
        help="The new user's roles [comma seperated].")
@click.option('--teams', '-t', required=True,
        help="The new user's teams [comma seperated].")
def create(email, first_name, last_name, roles, teams):
    user = User()
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.roles = [r.strip() for r in roles.split(',')]
    user.teams = [t.strip() for t in teams.split(',')]
    user.save()

@user.command()
@click.option('--username', '-u', required=True,
        help="The username of the user to delete")
def delete(username):
    user = User(username=username)
    user.delete()

@user.command()
@click.option('--username', '-u', required=True,
        help="The existing user's username.")
@click.option('--first-name', '-n',
        help="New value for the existing user's first name.")
@click.option('--last-name', '-l',
        help="New value for the existing user's last name.")
@click.option('--roles', '-r',
        help="New value for the existing user's roles [comma seperated].")
@click.option('--teams', '-t',
        help="New value for the existing user's teams [comma seperated].")
def update(username, first_name=None, last_name=None, roles=None, teams=None):
    user = User(username=username)
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    if roles:
        user.roles = roles.split(',')
    if teams:
        user.teams = teams.split(',')
    user.save()

