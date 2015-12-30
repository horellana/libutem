from setuptools import setup

setup(
    name='comprobar-estudiante',
    version='0.1.9',
    author='Hector Orellana',
    author_email='hofm92@gmail.com',
    url='https://github.com/juiko/comprobar-estudiante',
    license='GPL3',
    packages=['utem', 'utem.miutem', 'utem.dirdoc'],
    scripts=['bin/estudiante.py'],
    install_requires=['pyquery', 'requests']
)
