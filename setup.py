from setuptools import setup


setup(
    name='finding_min_subnet',
    version='1.0.0',
    description='App for finding the min subnet for a given set of IP addresses',
    packages=[''],
    entry_points={
        'console_scripts': [
            'run-ipv4 = find_subnet:main',
            'run-ipv6 = ind_subnet:main'
        ]
    },
    author='Denis Strigo',
    author_email='strigodenis@gmail.com',
    url='https://github.com/Den1sproger/Finding-subnet.git',
)


