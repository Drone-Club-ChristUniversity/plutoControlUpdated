from setuptools import setup, find_packages
import subprocess
import os

pypluto_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in pypluto_version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v,i,s = pypluto_version.split("-")
    pypluto_version = v + "+" + i + ".git." + s

assert "-" not in pypluto_version
assert "." in pypluto_version

assert os.path.isfile("pypluto/version.py")
with open("pypluto/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % pypluto_version)

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
