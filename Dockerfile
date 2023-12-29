FROM python:3.8

WORKDIR /IGFI

COPY files/requirements.txt

RUN pip install --no-cache-dir -r /IGFI/requirements.txt

COPY ..

WORKDIR /IGFI/scripts

EXPOSE 80

ENV IGFI production

CMD ["python", "igfi.py"]
