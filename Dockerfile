FROM ubuntu
FROM python:3.11

RUN apt update



WORKDIR /app
RUN mkdir /app/src

COPY ./deployment_requirements.txt /app/deployment_requirements.txt 

RUN pip install --no-cache-dir --upgrade -r deployment_requirements.txt

COPY ./models /app/models/
COPY ./src/prediction.py /app/src/prediction.py
COPY ./src/preprocessing.py /app/src/preprocessing.py
COPY ./app.py /app/app.py

CMD ["uvicorn", "app:app","--host", "0.0.0.0", "--port", "80"]