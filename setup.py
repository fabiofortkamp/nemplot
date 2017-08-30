from setuptools import setup, find_packages

setup(
    name='nemplot',
    version='0.1.3',
    packages=['nemplot'],
    description='Easier creation of matplotlib plots with standard formatting',
    license=open('LICENSE.md').read(),
    author='Fábio Fortkamp',
    author_email='fabio@fabiofortkamp.com',
    long_description=open('README.md').read(),
    install_requires=['numpy',
                      'matplotlib']
)
