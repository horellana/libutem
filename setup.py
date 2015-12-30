from setuptools import setup

setup(
    name='libutem',
    version='0.1.10',
    author='Hector Orellana',
    author_email='hofm92@gmail.com',
    url='https://github.com/juiko/libutem',
    license='GPL3',
    packages=['utem', 'utem.miutem', 'utem.dirdoc'],
    scripts=['bin/estudiante.py'],
    install_requires=['pyquery', 'requests']
)
