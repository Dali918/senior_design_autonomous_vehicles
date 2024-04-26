from setuptools import find_packages, setup

package_name = 'homework2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dalitso',
    maintainer_email='dalitbanda@gmail.com',
    description='basic implementation of server-client',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = homework2.navigation:main',
            'client = homework2.client:main'
        ],
    },
)
