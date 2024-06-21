from setuptools import find_packages, setup

package_name = 'ps5_controller'

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
    maintainer='teng',
    maintainer_email='teng@todo.todo',
    description='ROS 2 package for interfacing with PS5 controller through Bluetooth',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ps5_controller_node = ps5_controller.ps5_controller:main'
        ],
    },
)
