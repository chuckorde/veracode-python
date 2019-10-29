import sys
import os, stat
import json
import getpass

def make_config():
    username = input('Veracode API username: ')
    password = getpass.getpass('Veracode API password: ')
    password2 = getpass.getpass('Veracode API password (again): ')

    if password != password2:
        sys.exit('Passwords do not match.')

    if not (username or password):
        sys.exit('missing username or password')

    config_dir = os.path.expanduser('~/.veracode')
    if not os.path.exists(config_dir):
            os.mkdir(config_dir)

    config = {'username':username, 'password':password}
    config_file = os.path.join(config_dir, 'api-credentials.json')
    json.dump(config, open(config_file, 'w'))
    # race condition, any sugestions?
    os.chmod(config_file, stat.S_IREAD|stat.S_IWRITE)
    sys.exit('config created successfully')

if __name__ == '__main__':
    make_config()
