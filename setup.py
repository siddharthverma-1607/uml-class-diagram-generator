from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name="uml-class-diagram-generator",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'generate-uml=uml-generator.main:main',
        ],
    },
    install_requires=[],
    include_package_data=True,
    description="A tool to generate UML Class Diagrams from Python source code.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Siddharth Verma",
    author_email="siddharthverma.er.cse@gmail.com",
    url="https://github.com/siddharthverma-1607/uml-class-diagram-generator.git ", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
