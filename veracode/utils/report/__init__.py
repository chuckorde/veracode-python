import json
import datetime
import click
from tabulate import tabulate

def display(data, headers, format):
    if format == 'json':
        json_data = []
        for datum in list(data):
            user_data = {}
            for idx, header in enumerate(headers):
                header = header.replace(' ', '_').lower()
                d = datum[idx]
                if isinstance(d, datetime.date):
                    d = d.strftime('%Y-%m-%d')
                user_data[header] = d
            json_data.append(user_data)
        click.echo(json.dumps(json_data, indent=4))
    elif format == 'list':
        for idx, header in enumerate(headers):
            click.echo('{0:20} {1}'.format(header, data[0][idx]))
    else:
        click.echo(tabulate(data, headers=headers, tablefmt=format))

