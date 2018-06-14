from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='{{cookiecutter.python_module}}',
    py_modules=['{{cookiecutter.python_module}}'],
    version='0.1.0',
    description='Python for the {{cookiecutter.transformer_name}} transformer in FME',
    long_description=readme,
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_name}}',
    url='{{cookiecutter.fme_hub_url}}',
    install_requires=[
    ],
    keywords='fme fmepy transformer',
    classifiers=[
        'DO NOT UPLOAD TO PYPI',
        'Framework :: FME',
        'Development Status :: 4 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    zip_safe=False,
)