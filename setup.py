import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
        name = 'veracode-python',
        packages = setuptools.find_packages(),
        version = '0.1.49',
        license = 'MIT',
        description = 'Python wrapper for the Veracode APIs',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author = 'Chuck Orde',
        author_email = 'chuckorde@gmail.com',
        url = 'https://github.com/chuckorde/veracode-python',
        download_url = 'https://github.com/chuckorde/veracode-python/archive/v0.1.49.tar.gz',
        keywords = ['Veracode', 'Security'],
        install_requires=[
            'lxml',
            'python-dateutil',
            'requests',
            'strconv',
            'xmltodict',
        ],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
         ],
        python_requires='>=3.5',
)

