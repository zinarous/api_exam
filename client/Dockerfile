FROM frolvlad/alpine-python3
COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt --no-cache-dir
ADD . /client/
WORKDIR /client/