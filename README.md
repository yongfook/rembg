```
docker stop $(docker ps -aq)
docker rm $(docker ps -a -q)
docker image prune -f -a
docker pull yongfook/bg-remove:latest
docker run -d -p 8000:8000 --restart unless-stopped yongfook/bg-remove:latest
```