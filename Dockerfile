FROM python:latest
LABEL maintainer="bhattacharya.dhiman"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
