from setuptools import setup, find_packages


setup(
	name='task-bookkeeping',
	version='1.0.0',
	description='Console accounting',
	license='MIT',
	author='Putrin Evgeniy',
	author_email='evgeniy.putrin@gmail.com',
	packages=find_packages(),
	package_data={
		'task_bookkeeping': ['resources/*'],
	},
	entry_points={
		'console_scripts': [
			'accounting=task_bookkeeping:main',
		],
	},
	install_requires=[
		'appdirs>=1.4',
		'prettytable>=0.7',
	]
)