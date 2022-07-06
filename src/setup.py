from setuptools import setup, find_packages

data = dict(
    name="Dev",
    version="0.0.1",
    packages=find_packages(include=['library*']),
)

if __name__ == '__main__':
    setup(**data)
