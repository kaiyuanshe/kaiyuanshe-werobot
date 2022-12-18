# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import versioneer

with open('README.md') as f:
    readme = f.read()

with open('HISTORY.md') as f:
    history = f.read()


requirements = [
    # to specify what a project minimally needs to run correctly
]


setup(
    name="kaiyuanshe-werobot",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="开源社公众号后台",
    long_description=readme + '\n\n' + history,
    author="Ginta",
    author_email="775650117@qq.com",
    keywords="kaiyuanshe_werobot",
    # TODO myblog url
    # url="https://ginta.top",
    include_package_data=True,
    packages=find_packages(include=["kaiyuanshe_werobot", "kaiyuanshe_werobot.*"]),
    install_requires=requirements,
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "k-werobot = kaiyuanshe_werobot.__main__:main"
        ]
    },
)
