from setuptools import setup, Extension
import os


ext_modules = []
if compiler_available:
    ext_modules.append(Extension('fibonacci', ['fibonacci.c']))
# Check if the compiler is available
compiler_available = 'COMPILER_AVAILABLE' in os.environ and os.environ['COMPILER_AVAILABLE'] == '1'

ext_modules = []
if compiler_available:
    ext_modules.append(Extension('fibonacci', ['fibonacci.c']))

setup(
    name='c_extension_t',
    version='',
    packages=[''],
    url='',
    license='',
    author='amr2023',
    author_email='',
    description='',
    ext_modules=ext_modules
)
