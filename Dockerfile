FROM python:3.8-slim

WORKDIR /IGFI

COPY . /IGFI

RUN pip install --no-cache-dir -r files/requirements.txt

EXPOSE 5000

ENV NAME IGFI

CMD ["python", "igfi.py"]
