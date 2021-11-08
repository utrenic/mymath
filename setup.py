from setuptools import setup

setup(
    name='mymath',
    version='0.1',
    description='a silly math package',
    author='Kelvin Leung',
    author_email='kelvin619@gmail.com',
    url='https://github.com/utrenic/mymath',
    project_urls={
        "Bug Tracker": "https://github.com/utrenic/mymath/issues",
    },
    classifier=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    packages=['mymath', 'mymath.adv'],
)
    
