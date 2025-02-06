from setuptools import setup, find_packages

setup(
    name="genpasswd",  # Package name
    version="0.1.0",    # Version number
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        "flask>=2.0.0",  # List your dependencies here
        "requests>=2.26.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",  # Development dependencies
            "black>=21.0",
        ],
    },
    python_requires=">=3.8",  # Python version requirement
    entry_points={
        "console_scripts": [
            "my_script=my_project.module1:main",  # Create executable scripts
        ],
    },
)