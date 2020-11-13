from setuptools import setup
with open("README.MD","r") as fh:
    long description =fh.read()
setup(
    name='helloworld',
    version='0.0.1',
    description='Say hello!',
    py_modules=["helloworld"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Licence :: OSI Approved :: GNU General Public Licence v2 or later (GPLv2+)",
        "Operating System :: OS Independent"
        
    ],
    long description=long_description,
    long description_content_type="text/markdown",
    install_requires=[
        "blessings~=1.7",
    ],
    extras_require={
        "dev":[
            "pytest>=3.7",
        ],
    },

)