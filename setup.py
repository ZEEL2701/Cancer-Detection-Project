import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Cancer-Detection Project"
AUTHOR_USER_NAME = "ZEEL27"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "zeel7158@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/ZEEL27/Cancer-Detection Project",
    project_urls={
        "Bug Tracker": f"https://github.com/Zeel27/Cancer-Detection Project/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)