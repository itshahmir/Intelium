from setuptools import setup, find_packages

with open('README.MD', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='intelium',
    version='2.1.0',
    author='Ali Shahmir Khan',
    author_email='shahmirkhanutmanzai@gmail.com',
    description='A Python module for automating interactions to mimic human behavior in standalone apps or browsers when using Selenium, Pyppeteer, or Playwright.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Leadrive/intelium',
    project_urls={
        'Bug Tracker': 'https://github.com/Leadrive/intelium/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['asyncio', 'HumanCursor', 'keyboard'],
    python_requires='>=3.6'
)