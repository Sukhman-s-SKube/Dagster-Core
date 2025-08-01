from setuptools import find_packages, setup

setup(
    name="dagster_skube",
    packages=find_packages(exclude=["dagster_skube_tests"]),
    install_requires=[
        "dagster[postgres,aws]>=1.4.0,<2.0",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
