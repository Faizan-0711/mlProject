from setuptools import find_packages,setup



setup(

    name ='mlProject',
    version = '0.0.1',
    author = 'Faizan',
    author_email = 'faizanfahim8584@gmail.com',
    packages = find_packages(),
    install_requires =get_requirements('requirements.txt')
)
