import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
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
)
