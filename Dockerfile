
FROM python:3.10


WORKDIR /app

COPY ./requirements.txt /app/requirements.txt 

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./models/XGB.joblib /app/models/XGB.joblib
COPY ./src/prediction.py /app/src/prediction.py
COPY ./src/preprocessing.py /app/src/preprocessing.py
COPY ./app.py /app/app.py
EXPOSE 80
CMD ["uvicorn", "app:app","--host", "0.0.0.0", "--port", "80"]