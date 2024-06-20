from setuptools import setup, find_packages

setup(
    name='cars',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',  # ou a versão específica do Django que você está usando
    ],
    entry_points={
        'console_scripts': [
            'manage=cars.manage:main',
        ],
    },
)
