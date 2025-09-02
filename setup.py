from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="jigglypuff",
    version="1.0.0",
    author="trose",
    author_email="trose@example.com",
    description="AI-Controlled Mouse Activity Manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trose/jigglypuff",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "jigglypuff=mcp_server:main",
        ],
    },
    scripts=["jiggly_puff.sh"],
)