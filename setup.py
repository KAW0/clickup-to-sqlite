from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="clickup-to-sqlite",
    description="Save data from ClickUp to a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Gregor Müllegger",
    url="https://github.com/gregmuellegger/clickup-to-sqlite",
    project_urls={
        "Issues": "https://github.com/gregmuellegger/clickup-to-sqlite/issues",
        "CI": "https://github.com/gregmuellegger/clickup-to-sqlite/actions",
        "Changelog": "https://github.com/gregmuellegger/clickup-to-sqlite/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["clickup_to_sqlite"],
    entry_points="""
        [console_scripts]
        clickup-to-sqlite=clickup_to_sqlite.cli:cli
    """,
    install_requires=[
        "sqlite-utils>=2.4.2",
        # "requests-oauthlib~=1.2.0",
        # "python-dateutil",
    ],
    extras_require={"test": ["pytest"]},
    tests_require=["clickup-to-sqlite[test]"],
)
