import setuptools

with open("README.md", "r") as description:
    long_description = description.read()

setuptools.setup(
    name="discogs-marketplace-scraper",
    version="0.0.1",
    author="Romanas Grigorjevas",
    author_email="romanas@grigorjevas.com",
    description="Discogs marketplace scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "asttokens==2.0.4",
        "attrs==20.3.0",
        "beautifulsoup4==4.11.1",
        "certifi==2020.12.5",
        "chardet==4.0.0",
        "colorama==0.4.4",
        "executing==0.5.4",
        "jedi==0.16",
        "icecream==2.1.0",
        "idna==2.10",
        "iniconfig==1.1.1",
        "numpy==1.21.0",
        "packaging==21.3",
        "pandas==1.5.3",
        "pluggy==0.13.1",
        "py==1.10.0",
        "Pygments==2.13.0",
        "pyparsing==2.4.7",
        "pytest==6.2.2",
        "python-dateutil==2.8.2",
        "pytz==2022.5",
        "requests==2.26",
        "six==1.15.0",
        "soupsieve==2.2",
        "toml==0.10.2",
        "urllib3==1.26.3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Intependent"
    ],
    python_requires=">=3.6"
)
