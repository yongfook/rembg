import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="rembg",
    version="1.0.9",
    description="Remove image background",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.5, <4",
    entry_points={
        "console_scripts": [
            "rembg=rembg.cmd.cli:main",
            "rembg-server=rembg.cmd.server:main",
        ],
    },
)
