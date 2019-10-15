#!/bin/bash

#This script is designed to quickl;y rebuild a dockerfile by purging the corrent containers associated with it and rerunning

containerID=$(docker ps -a | awk '{print$1}' | awk NR==2)
docker stop ${containerID}
docker system prune -f
imageID=$(docker build . | grep 'Successfully built' | awk '{print$3}')
docker run -d -it -p 5000:5000 ${imageID}

