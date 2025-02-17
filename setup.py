import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="swarmprediction",
    version="0.0.1",
    description="Ensembles for prediction powered by agentic systems",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/swarmprediction",
    author="microprediction",
    author_email="peter.cotton@microprediction.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=["swarmprediction"],
    test_suite='pytest',
    tests_require=['pytest','pandas','scipy>=1.7.3','randomcov'],
    include_package_data=True,
    install_requires=["numpy","pytest"],
    entry_points={
        "console_scripts": [
            "swarmprediction=swarmprediction.__main__:main",
        ]
    },
)
