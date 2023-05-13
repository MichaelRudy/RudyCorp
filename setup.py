import os
from setuptools import setup

setup(name='rudycorp',
    version='0.0.1',
    description='Personal website for deploying and displaying my projects, interests and hobbies.',
    author='Michael Rudy',
    license='MIT',
    packages=['rudycorp', 'rudycorp.static', 'rudycorp.templates'],
    classifiers=[
        "Programming Languag :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=['flask', 'requests'],
    python_requires='>=3.8',
    )