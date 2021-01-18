from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__project__ = "ambientco2"
__version__ = "0.0.3"
__description__ = "Python module for CozIR Ambient CO2 sensors"
__packages__ = ["ambientco2"]
__long_description__ = long_description
__long_description_content_type__ = "text/markdown"
__author__ = "Michael Jack"
__author_email__ = "50518949+mjackdk@users.noreply.github.com"
__url__ = "https://github.com/mjackdk/PythonCO2"
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]
__keywords__ = ["sensor","CO2","Ambient","CozIR"]
__requires__ = ["serial"]
__python_requires__ = '>=3.6'

setup(
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    long_description = __long_description__,
    long_description_content_type = __long_description_content_type__,
    author = __author__,
    author_email = __author_email__,
    url = __url__,
    classifiers = __classifiers__,
    keywords = __keywords__,
    requires = __requires__,
    python_requires = __python_requires__,
)
