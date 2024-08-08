import setuptools

setuptools.setup(
    name="converters",
    version="0.0.1",
    author="Test Author",
    author_email="test@example.com",
    description="Demo package with temperature conversion functions.",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where="src"),
)
