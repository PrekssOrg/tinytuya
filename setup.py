import setuptools
import importlib.metadata
import re
import os

# Read version string directly without importing the module
with open(os.path.join("tinytuya", "__init__.py"), "r", encoding="utf-8") as f:
    version_match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", f.read(), re.M)
    if version_match:
        __version__ = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    'requests',      # Used for Setup Wizard - Tuya IoT Platform calls
    'colorama',      # Makes ANSI escape character sequences work under MS Windows.
]

CHOOSE_CRYPTO_LIB = [
    'cryptography',  # pyca/cryptography - https://cryptography.io/en/latest/
    'pycryptodome',  # PyCryptodome      - https://pycryptodome.readthedocs.io/en/latest/
    'pyaes',         # pyaes             - https://github.com/ricmoo/pyaes
    'pycrypto',      # PyCrypto          - https://www.pycrypto.org/
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
