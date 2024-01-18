from subprocess import check_output

from setuptools import find_packages, setup

requirements = []
with open('./requirements.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        if not line.startswith('git+ssh'):
            requirements.append(line)

test_requirements = []
with open('./requirements-dev.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        if not line.startswith('git+ssh') and not line.startswith('--index'):
            test_requirements.append(line)

try:
    VERSION = (
        check_output(['git', 'describe', '--tags']).rstrip().decode().replace('v', '')
    )
except Exception as e:  # pylint: disable=broad-except
    print(e)
    VERSION = '1.0.0'


setup(
    author='Simon Kuhball',
    author_email='simon@kuhball.de',
    python_requires='>=3.11',
    description='leuchten app',
    install_requires=requirements,
    include_package_data=True,
    keywords='leuchten',
    name='leuchten',
    packages=find_packages(include=['leuchten', 'leuchten.*']),
    test_suite='tests',
    tests_require=test_requirements,
    version=VERSION,
    zip_safe=False,
)
