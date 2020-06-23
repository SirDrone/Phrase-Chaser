from setuptools import setup

setup(
	name='Sanitized_CSV_Creator',
	url='https://github.com/SirDrone/CSV-Sanitizer',
	author='***REMOVED***',
	author_email='alexkirk95@gmail.com',
	packages=['sanitization_pack'],
	install_requires=['pandas'],
	version='1.1',
	license='SirDrone',
	description='Automatically creates sanitized CSVs based on existing CSVs in folder',
	long_description=open('README.txt').read(),
)
