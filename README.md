# Docker Container Example

This repository contain a Python example with Docker container. This project
is used to example how run application's container inside Jenkins Pipelines.

It has dependency with Database container. That db container is used by
linking function provided by Docker.

## How to run

```shell
docker build -t jenkins-container-example  .
```

Inside Jenkins you should setup a `shell` command like that:

```shell
docker run -it --rm --name ${BUILD_ID}-jenkins-example jenkins-container-example
docker inspect ${BUILD_ID}-jenkins-example --format=\"{{ .State.Health.Status }}\"
```

