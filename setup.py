from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Pagepulse"
AUTHOR_USER_NAME = "Swayam96"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Swayam Prajapati",
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Swayam96/Pagepulse",
    author_email="swayam.prajapati.200496@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
