import setuptools
import sys
import os
import io
import re

###############################################################################

name = 'veracode-python'
description = 'Python wrapper for the Veracode XML APIs'
install_requires = [
    'lxml>=4.4.1',
    'python-dateutil>=2.8.1',
    'requests>=2.22.0',
    'strconv>=0.4.2',
    'xmltodict>=0.12.0',
    'Click>=7.0',
    'tabulate>=0.8.6',
]
keywords = []
entry_points = {'console_scripts': [
    'veracode-cli=veracode.old:main',
    'veracode=veracode.utils.cli:main'
    ]}
python_requires='>= 3.5'

author = 'Chuck Orde'
author_email = 'chuckorde@gmail.com'
repo_user = 'chuckorde'

license = 'BSD-3-Clause'
classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
 ]

repo_name = name

repo_url = 'https://github.com/{}'
download_url = '{}/archive/v{}/.tar.gz'
release_api_url = 'https://api.github.com/repos/{}/{}/releases?access_token={}'

###############################################################################

# >>> python setup.py -q version
# 0.1.0
# >>> python setup.py -q version -i patch
# 0.1.1
# >>> python setup.py -q version -i minor
# 0.2.0

# -q turns off 'running version' output

class Version(setuptools.Command):
    version_re = r"__version__ = '(.*?)'"
    user_options = [ ('increment=', 'i', None), ]

    def initialize_options(self):
        self.increment = None

    def finalize_options(self):
        pass

    def run(self):
        if self.increment:
            self._increment_semantic_version()
        print(self.get())

    def _increment_semantic_version(self):
        current_version = self.get()
        (major, minor, patch) = [int(n) for n in current_version.split('.')]
        release = self.increment.upper()
        assert(release in ['MAJOR', 'MINOR', 'PATCH'])
        if release == 'PATCH': patch = patch + 1
        if release == 'MINOR': minor = minor + 1; patch = 0
        if release == 'MAJOR': major = major + 1; minor = 0; patch = 0

        new_version = '{}.{}.{}'.format( major, minor, patch)
        with io.open(self._find_init_file(), 'r', encoding='utf8') as f:
            init_file = f.read()

        with io.open(self._find_init_file(), 'w', encoding='utf8') as f:
            f.write(init_file.replace(current_version, new_version))

    def _find_init_file(self):
        for walk in os.walk('.'):
            (path, directory, module) = walk
            if '__init__.py' in module:
                return os.path.join(path, '__init__.py')

    @classmethod
    def get(self):
        with io.open(self._find_init_file(self), 'r', encoding='utf8') as f:
            version = re.search(self.version_re, f.read()).group(1)
        return version


class Github(setuptools.Command):
    user_options = [ ('create-release=', 'r', None), ]

    def initialize_options(self):
        self.create_release = None

    def finalize_options(self):
        pass

    def run(self):
        if not self.create_release:
            raise Exception('You must specifiy --release=<API TOKEN>')

        import requests
        version = Version.get()
        json = {
            "tag_name": "v{}".format(version),
            "target_commitish": "master",
            "name": "v{}".format(version),
            "body": "Release v{}".format(version),
            "draft": False,
            "prerelease": False
        }
        api_url = release_api_url.format(
                repo_user, repo_name, self.create_release)
        res = requests.post(api_url, json=json)
        print (res.status_code, res.json())


version = Version.get()
url = '{}/{}'.format(repo_url.format(repo_user), repo_name)
download_url = download_url.format(url, version)

with io.open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name = name,
    packages = setuptools.find_packages(),
    version = version,
    license = license,
    description = description,
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = author,
    author_email = author_email,
    url = url,
    download_url = download_url,
    keywords = keywords,
    install_requires = install_requires,
    classifiers = classifiers,
    python_requires = python_requires,
    cmdclass = { 'version': Version, 'github': Github },
    entry_points = entry_points,
)

