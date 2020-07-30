import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-RhysGrabany", # Replace with your own username
    version="0.0.2",
    author="Rhys Grabany",
    author_email="r.grabany@gmail.com",
    description="Simple Maze Creation Program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RhysGrabany/maze-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)