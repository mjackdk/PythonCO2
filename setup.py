import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ambientco2", # Replace with your own username
    version="0.0.1",
    author="Michael Jack",
    author_email="mjpub@me.com",
    description="Python module for CozIR Ambient CO2 sensors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mjackdk/PythonCO2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
