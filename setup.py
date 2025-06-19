from setuptools import setup, find_packages

setup(
    name="apis",
    version="0.1.0",
    description="Reusable data structures",
    author="Aleksandr Soloshenko",
    packages=find_packages(),
    install_requires=[
        "pydantic",
    ],
    python_requires=">=3.8",
)
