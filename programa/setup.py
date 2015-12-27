from setuptools import setup, find_packages

setup(
    name='comprobar-estudiante',
    version='0.1.0',
    author='Hector Orellana',
    author_email='hofm92@gmail.com',
    url='https://github.com/juiko/comprobar-estudiante',
    license='GPL3',
    packages=['miutem'],
    package_dir={'miutem': 'src/miutem'},
    scripts=['bin/estudiante.py'],
    install_requires=['pyquery', 'requests']
)
