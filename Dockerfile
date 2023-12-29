FROM python:3.8

WORKDIR /IGFI

COPY . /IGFI

WORKDIR /IGFI/scripts

RUN pip install --no-cache-dir -r /IGFI/requirements.txt

EXPOSE 80

ENV IGFI production

CMD ["python", "IGFI.py"]
