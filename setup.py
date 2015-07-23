from setuptools import setup, find_packages
from genpass import VERSION, __author__, __email__


setup(
    name='genpass',
    version=VERSION,
    packages=find_packages(),

    author=__author__,
    author_email=__email__,
    keywords='hacker tools, password, social engineering',
    description='generate the password of person',
    url='https://github.com/RicterZ/genpass',
    include_package_data=True,
    zip_safe=False,

    entry_points={
        'console_scripts': [
            'genpass = genpass.command:main',
        ]
    },
    license='MIT',
)
