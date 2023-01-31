import setuptools

long_desc = open("README.md").read()

setuptools.setup(
    name="Isobox",
    version="<VERSION_NUMBER>",  # eg:1.0.0
    author="Solirs",
    author_email="iusegentoobtw@protonmail.com",
    license="GPLv3",
    description="Run a linux live iso inside a chroot jail!",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/Solirs/Isobox",
    packages=setuptools.find_packages(where="."),
    scripts=["isobox.py"],
)
