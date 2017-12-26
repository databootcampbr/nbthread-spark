# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name="nbthread_spark",
    version="0.0.5",
    description="Spark Structured Streaming multithread in IPython Notebooks",
    long_description=open('README.rst').read(),
    author="Data Bootcamp",
    author_email="contato@databootcamp.com.br",
    license='Apache',
    dependency_links = ['git+https://github.com/micahscopes/nbmultitask.git@master#egg=nbmultitask-0'],
    install_requires=[
        "nbmultitask",
        "ipywidgets==7.0.5",
        "pyspark"
    ],
    packages=find_packages(),
)
