from setuptools import setup, find_packages

setup(
    name="foundationpose",
    version="0.1.0",
    description="A unified foundation model for 6D object pose estimation and tracking",
    author="Bowen Wen, Wei Yang, Jan Kautz, Stan Birchfield",
    url="https://github.com/NVlabs/FoundationPose",
    packages=find_packages(),
    python_requires=">=3.9",
    # install_requires=requirements,
)