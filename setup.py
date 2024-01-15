from io import open
from setuptools import setup
from auto_py_to_exe import __version__ as version

setup(
    name='blueiris-overlay-macros-yandex-weather',
    version=version,
    url='https://github.com/vladimirpichugin/blueiris-overlay-macros-yandex-weather',
    license='',
    author='Vladimir Pichugin',
    author_email='vladimir@pichug.in',
    description='',
    long_description=''.join(open('README.md', encoding='utf-8').readlines()),
    long_description_content_type='text/markdown',
    keywords=['gui', 'executable'],
    packages=['auto_py_to_exe'],
    include_package_data=True,
    install_requires=['requirements'],
    python_requires='>=3.10',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'main=main.__main__:main'
        ],
    },
)
