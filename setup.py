# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name="nbthread_spark",
    version="0.0.2",
    description="Spark Streaming multithread in IPython Notebooks",
    long_description=open('README.rst').read(),
    author="Data Bootcamp",
    author_email="contato@databootcamp.com.br",
    license='Apache',
    dependency_links = ['git+https://github.com/micahscopes/nbmultitask.git@master#egg=nbmultitask-0'],
    install_requires=[
        "nbmultitask",
        "ipywidgets==7.0.5"
    ],
    packages=find_packages(),
)
