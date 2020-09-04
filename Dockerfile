FROM python:3

ADD /src /src
ADD requirements.txt /
ADD setup.py /
WORKDIR /

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

CMD rembg-server -p 8000