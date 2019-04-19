import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LJW",
    version="2.1.0",
    author="Jaewoo Lee",
    author_email="doni04164@gmail.com",
    description="All About LJW",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaewoo4200/poem_LJW",
    python_requires = '>=3.0',
    #packages=setuptools.find_packages(),
    packages=['LJW'],
    classifiers=[
        "Programming Language :: Python :: 3.0",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
