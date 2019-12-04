from setuptools import setup


setup(
    name='me-clie',
    version='1.0',
    author='Nigel Millward',
    author_email='nigel.millward@gmail.com',
    description='ME command line interface',
    entry_points='''
    [console_scripts]
    me=me:entry_point
    ''',
)