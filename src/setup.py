from setuptools import setup, find_packages

data = dict(
    name="pyDev",
    version="0.2.3",
    packages=find_packages(include=['pyDev*']),
)

if __name__ == '__main__':
    setup(**data)
