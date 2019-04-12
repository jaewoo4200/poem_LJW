import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LJW",
    version="0.0.1",
    author="Jaewoo Lee",
    author_email="doni04164@gmail.com",
    description="Korean poets written by LJW",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaewoo4200/poem_LJW",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
