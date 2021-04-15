FROM python:3.7-alpine
WORKDIR /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
ENTRYPOINT ["python3"]
CMD ["api_final.py"]