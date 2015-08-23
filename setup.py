from setuptools import setup, find_packages

setup(
    name="hello",
    version="1.0",
    description="Template package for Python",
    author="Andreea Lucau",
    author_email="andreea.lucau@gmail.com",
    packages=find_packages("src"),
    package_dir = {
        "": "src",
    },
    package_data = {
        "hello": ["data/greeting_templates.txt"],
    },
    test_suite="tests",
    install_requires=["setuptools", "Sphinx"],
)