FROM python:3.8-slim

LABEL maintainer="new92 new92github@gmail.com"
LABEL description=""

WORKDIR /IGFI

COPY files/requirements.txt

RUN pip install --no-cache-dir -r files/requirements.txt

COPY ..

EXPOSE 5000

ENV IGFI production

CMD ["python", "igfi.py"]
