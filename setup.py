import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="noteline-sdk",
    version="1.1.1",
    author="Viacheslav Kovalevskyi",
    author_email="viacheslav@kovalevskyi.com",
    description="SDK for manipulating noteline specific metadata of the Notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/noteline-org/noteline-sdk",
    packages=setuptools.find_packages(),
    install_requires=[
        'nbformat'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
