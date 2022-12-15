from setuptools import setup

setup(
    name='software_release_install_tools',
    version='0.1.0',
    packages=['UFObase_installer'],
    entry_points={
        'console_scripts': [
            'UFObase_installer = UFObase_installer:main',
        ]
    },
    description='',
    test_suite='tests',
    install_requires=['PySimpleGUI', 'pywin32'],
    python_requires='>=3.6'
)
