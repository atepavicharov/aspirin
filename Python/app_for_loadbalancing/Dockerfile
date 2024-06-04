FROM python:3-slim

WORKDIR /usr/src/app

COPY app/ ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "fastapi", "run", "./api_main.py", "--port", "80"]