import sys
import os
# Ensure the local folder is searched first
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import setuptools
import importlib.metadata
from tinytuya import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    'requests',      
    'colorama',      
]

CHOOSE_CRYPTO_LIB = [
    'cryptography',  
    'pycryptodome',  
    'pyaes',         
    'pycrypto',      
]

pref_lib = CHOOSE_CRYPTO_LIB[0]
for cryptolib in CHOOSE_CRYPTO_LIB:
    try:
        importlib.metadata.version(cryptolib)
        pref_lib = cryptolib
        break
    except importlib.metadata.PackageNotFoundError:
        pass

INSTALL_REQUIRES.append(pref_lib)

setuptools.setup(
    name="tinytuya",
    version=__version__,
    author="Jason Cox",
    author_email="jason@jasonacox.com",
    description="Python module to interface with Tuya WiFi smart devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jasonacox/tinytuya',
    packages=setuptools.find_packages(exclude=("sandbox",)),
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
