from setuptools import setup, find_packages

setup(
    name='tsp-planner',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'pika',
        'ortools',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'tsp_planner = src.main:main'
        ]
    },
    author='CoolBlue Planning Tech',
    description='A service for solving the Traveling Salesman Problem using OR-tools library',
    url='https://github.com/ghorbani-mohammad/travelling-salesman-problem'
)
