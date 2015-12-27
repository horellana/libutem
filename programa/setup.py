from setuptools import setup

setup(
    name='comprobar-estudiante',
    version='0.1.7',
    author='Hector Orellana',
    author_email='hofm92@gmail.com',
    url='https://github.com/juiko/comprobar-estudiante',
    license='GPL3',
    packages=['miutem'],
    package_dir={'miutem': 'src/miutem'},
    scripts=['bin/estudiante.py'],
    install_requires=['pyquery', 'requests']
)
