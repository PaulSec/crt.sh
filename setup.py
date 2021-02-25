from setuptools import setup

setup(
    name='crtsh',
    author='PaulSec',
    version='0.3.1',
    packages='.',
    description='(Unofficial) Python API for https://crt.sh',
    install_requires=["requests"],
    url = 'https://github.com/PaulSec/crt.sh',
    download_url = 'https://github.com/PaulSec/crt.sh/archive/0.3.1.tar.gz',
    keywords = ['crt.sh', 'ssl', 'certificates', 'osint'],
)