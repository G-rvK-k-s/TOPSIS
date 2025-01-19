from setuptools import setup, find_packages

setup(
    name="102217006-topsis",  
    version="1.0.5",
    author="ANMOL BHATT",
    description="A Python package for implementing the TOPSIS multi-criteria decision analysis method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  
    packages=find_packages(),  
    install_requires=[
        "numpy",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",  
)
