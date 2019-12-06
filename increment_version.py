import semantic_version
import re
import git

version_files = ['setup.py', 'veracode/__init__.py']

actions = {
    'PATCH': 'next_patch',
    'MINOR': 'next_minor',
    'MAJOR': 'next_major'
}

def update_version(doc, version_function):
    with open(doc) as setup:
        lines = setup.read()
        version = re.search('\d\.\d\.\d', lines).group()
        version = semantic_version.Version(version)
        version = getattr(version, version_function)()
        lines = re.sub('\d\.\d\.\d', f'{version}', lines)

    with open(doc,'w') as setup:
        setup.write(lines)
        return version

repo = git.Repo('.')
version_index = repo.head.commit.message.split(':')

if len(version_index) == 2:
    version_index = version_index[0].upper()
    version_function = actions.get(version_index)
    if not version_function:
        raise Exception('Commit message contains an unknown index!')
    for version_file in version_files:
        version = update_version(version_file, version_function)
else:
    raise Exception('Refusing to deploy without incrementing version')

print(version)
