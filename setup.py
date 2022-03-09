from setuptools import setup

setup(
    name='powertochoosetx',
    url='https://github.com/deino475/powertochoosetx',
    author='Nile Dixon',
    author_email='niledixon475@gmail.com',
    packages=['powertochoosetx'],
    install_requires=['requests'],
    version='0.5.0',
    license='GNU GPL-V2',
    description='An unofficial Python wrapper for the TX Power To Choose API',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6"
)

