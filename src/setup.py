from setuptools import setup, find_packages

data = dict(
    name="src",
    version="0.1",
    packages=find_packages(),
)

if __name__ == '__main__':
    setup(**data)
