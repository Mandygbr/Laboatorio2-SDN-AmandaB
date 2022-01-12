FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY Laboratorio2.py./

CMD [ "python", "Laboratorio2.py" ]