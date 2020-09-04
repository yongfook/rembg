```
docker stop $(docker ps -aq)
docker rm $(docker ps -a -q)
docker image prune -f -a
docker pull yongfook/bg-remove:latest
docker run -d -p 8000:8000 --env ML_AUTH_KEY --restart unless-stopped yongfook/bg-remove:latest
```

Run Locally:
```
python3 -m pip install --no-cache-dir -r requirements.txt
python3 setup.py install
rembg-server -p 8000
```