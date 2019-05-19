from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'pySGDabao',
  packages = ['pySGDabao'],
  version = '1.0.1',
  license='Apache License 2.0',
  description = 'A library for your Singapore food delivery needs',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'rizemon',
  author_email = 'tan.jia.le.98@gmail.com',
  url = 'https://github.com/rizemon/pySGDabao',
  download_url = 'https://github.com/rizemon/pySGDabao/archive/v1.0.1.tar.gz',
  keywords = ['Foodpanda', 'Deliveroo', 'Honestbee'],
  install_requires=[
          'requests',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)