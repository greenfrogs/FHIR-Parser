import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='FHIR Parser',
    version='0.1.5',
    author='Greenfrogs',
    author_email='5961364+greenfrogs@users.noreply.github.com',
    description='An elegant and simple FHIR library for Python, built for human beings',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/greenfrogs/FHIR-Parser',
    license='Apache License 2.0',
    install_requires=['requests>=2.23.0', 'python-dateutil>=2.8.1'],
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)