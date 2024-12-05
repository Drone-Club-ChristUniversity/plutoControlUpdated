from setuptools import setup, find_packages
import subprocess
import os

def get_version():
    result = subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE, text=True)
    version = result.stdout.strip()
    if "-" in version:
        # Convert to PEP 440 compliant version
        v, i, s = version.split("-")
        version = v + "+" + i + ".git." + s
    return version

pypluto_version = get_version()

if not pypluto_version:
    raise ValueError("Version could not be determined from git tags.")

assert "-" not in pypluto_version, "Version format is incorrect"
assert "." in pypluto_version, "Version format is incorrect"

print("Version: ", pypluto_version)

setup(
    name='pypluto-christ',
    version=pypluto_version,
    packages=find_packages(),
    install_requires=[],
    author='Shrey Jain',
    author_email='shrey.jain@mca.christuniversity.in',
    description='A library for controlling Pluto drones for the Christ University projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Drone-Club-ChristUniversity/plutoControlUpdated.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)