from setuptools import find_packages, setup

with open("./README.md", "r") as f:
    long_description = f.read()

setup(
    name="django_hls",
    version="1.0.0",
    description="A package in Django for streaming video and audio using the HLS",
    packages=find_packages(where="django_hls"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YasinKar/django_hls",
    author="Yasin Karbasi",
    author_email="yasinkardev@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "bson >= 0.5.10",
        
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
    keywords="stream django hls",
)