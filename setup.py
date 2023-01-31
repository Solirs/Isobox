import setuptools

long_desc = open("README.md").read()

setuptools.setup(
    name="Isobox",
    version="0.1",
    author="Solirs",
    author_email="iusegentoobtw@protonmail.com",
    license="GPLv3",
    description="Run a linux live iso inside a chroot jail!",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/Solirs/Isobox",
    packages=["src"],
    package_dir={"src": "src/"},
    package_data={"src": ["shellscripts/*"]},
    scripts=["isobox"],
)
