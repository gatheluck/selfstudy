```
# Build and run container.
$ sudo docker build -t ct:0.1 .
$ sudo docker run --name ct -it -v $HOME/Docker:/home/tester/share ct:0.1

# Step into container.
$ sudo docker container exec -it ct bash

# Stop contrainer.
# docker stop ${container_id}
```