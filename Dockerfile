FROM python:3

WORKDIR /src/rembg

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install git+git://github.com/yongfook/rembg#egg=rembg

COPY . .

CMD rembg-server -p 8000