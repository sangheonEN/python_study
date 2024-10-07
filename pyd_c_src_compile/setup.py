from setuptools import setup, Extension

# Define the extension module
example_module = Extension(
    'example',
    sources=['example.c', 'example_module.c']
)

# Setup script to build the module
setup(
    name='example',
    version='1.0',
    description='Python Package with a C extension for adding two numbers',
    ext_modules=[example_module],
)
