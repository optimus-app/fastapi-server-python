# CICD Pipeline in Python

This is a template for any CICD Pipeline in Python. In this template, there are folders to be aware of:

- `src/`: This is where the source code of the project is located. The name should be changed to the repository's name. For example, if the repository is called `my-repo`, then the folder should be called `my-repo`.
- `tests/`: This is where the tests of the project are located. The structure should be the same as the `src/` folder.

There are files that should be aware of:

- `conftest.py`: This file is used to configure the tests. It is used to configure the `pytest` framework. It allows us to import the `src` folder in the tests.
- `Dockerfile`: This file is used to build the Docker image of the project.
- `gitlab-ci.yml`: This file is used to configure the GitLab CI/CD pipeline. It is used to build the Docker image and run the tests.