FROM python:3

COPY . /LABORATORIO
WORKDIR /LABORATORIO
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

VOLUME /LABORATORIO
COPY devices.csv /LABORATORIO

CMD [ "python","Laboratorio2.py" ]