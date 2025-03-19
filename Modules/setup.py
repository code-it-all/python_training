__version__ = "0.1.0"
from setuptools import setup, find_packages

setup(
    name="my_package",
    version=__version__,
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={"console_scripts": ["my_module=my_module.cli:main"]},
    author="Vrishti",
    author_email="riyavrishti@gmail.com",

)