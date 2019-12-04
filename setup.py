import setuptools

setuptools.setup(
    name="python-example",
    version="1.0",
    author="Bernd Doser",
    author_email="bernd.doser@h-its.org",
    description="A small example package",
    url="https://github.com/bernddoser/python-example",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)