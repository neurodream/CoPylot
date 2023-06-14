from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='orgshells',
    version='0.1',
    author='Nico Adelhöfer',
    author_email='nico.adelhoefer@ru.nl',
    description='collection of shell scripts to streamline issue-based, cooperative text/code-centered work',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/neuro-dream/orgshells',
    project_urls = {
        "Bug Tracker": "https://github.com/neuro-dream/orgshells/issues"
    },
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'your-package-name=your_package_name:main',
        ],
    },
)
