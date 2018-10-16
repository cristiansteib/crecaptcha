from setuptools import setup

setup(
    name='crecaptcha',
    version='0.1.3',
    author='Steib Cristian',
    author_email='cristiansteib@gmail.com',
    packages=['crecatpcha'],
    url='https://github.com/cristiansteib/crecatpcha/',
    license='LICENSE.txt',
    description='reCatpcha api v3.0 - with django support',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Flask",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security"
    ],
)
