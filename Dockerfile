FROM python:3.13.0a6-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /IGFI

COPY . /IGFI

RUN pip install --no-cache-dir -r files/requirements.txt

EXPOSE 4000

ENV NAME IGFI

CMD ["python", "igfi.py"]