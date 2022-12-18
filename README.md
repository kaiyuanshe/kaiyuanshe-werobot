kaiyuanshe-werobot
====

Features
--------
* package.sh should be finish in jenkins

Build image:
----
1. run sh package.sh to generate .whl
2. run docker build -t kaiyuanshe-werobot:0.1 . to build image(get version from versioneer) 
