FROM python:3

WORKDIR /src/rembg

COPY requirements.txt ./
COPY setup.py ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python3 setup.py install

COPY . .

CMD rembg-server -p 8000