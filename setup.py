from setuptools import setup

setup(
    name = 'rdflib-microdata',
    version = '0.2.0',
    description = "rdflib extension for parsing microdata into an rdf graph",
    author = "Ed Summers",
    author_email = "ehs@pobox.com",
    url = "http://github.com/edsu/rdflib-microdata",
    py_modules = ["rdflib_microdata"],
    test_suite = "test",
    install_requires = ["html5lib", "microdata>=0.2", "rdflib>=3.0"],
)
