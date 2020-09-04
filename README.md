```
docker stop $(docker ps -aq)
docker pull yongfook/bg-remove:latest
docker run -d -p 8000:8000 --restart unless-stopped yongfook/bg-remove
```