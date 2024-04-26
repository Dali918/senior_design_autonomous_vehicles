from setuptools import find_packages, setup

package_name = 'homework1'

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
    maintainer_email='dalitso@todo.todo',
    description='package for homework 1',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = homework1.talker:main',
            'listener = homework1.listener:main',
            'publisher = homework1.publisher:main',
            'subscriber = homework1.subscriber:main'
        ],
    },
)
