from setuptools import setup

setup(
    name='newpie',
    version='0.1',
    py_modules=['newpie'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        newpie=newpie:main
    ''',
)
