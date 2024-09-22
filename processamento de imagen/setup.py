from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_lucasfreitas",
    version="0.0.1",
    author="lucas",
    description="image processing package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/freitaslucas23/image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>3.5',

)