from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='template',
    version='0.1.0',
    description='template package',
    long_description=readme,
    author='Gabe Stier',
    author_email='gabezter@gmail.com',
    url="http://gitlab.home.network/templates/python",
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)