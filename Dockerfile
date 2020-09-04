FROM python:3

WORKDIR /src/rembg

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python setup.py install

COPY . .

CMD rembg-server -p 8000