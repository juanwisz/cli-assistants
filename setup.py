from setuptools import setup, find_packages

# Define your package's metadata and other options here
setup(
    name='cli-assistants',  # Your package name, should be unique on PyPI
    version='0.1.0',  # Start with a small version, following semantic versioning
    author='Juan Wisznia',  # Your name or your organization's name
    author_email='juanwisznia@gmail.com',  # Your email or your organization's contact email
    description='A small yet powerful script to invoke OpenAI Assistants through our CLI.',  # Short description of your package
    long_description=open('README.md').read(),  # Your README file's content
    long_description_content_type='text/markdown',  # Type of your README file's content
    url='https://github.com/juanwisz/cli-assistants',  # URL to your package's repository
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[
        # List your package's dependencies here
        # For example, if your package depends on requests, you'd put 'requests'
    ],
    entry_points={
        'console_scripts': [
            'gpt-assist=gpt_assistants_cli.script:main',  # Adjust the module path as necessary
        ],
    },
    classifiers=[
        # Choose your license as you wish
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',  # Specify the minimum Python version required
)

