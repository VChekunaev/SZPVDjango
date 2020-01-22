FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Project Files and Settings
ARG PROJECT=myproject
ARG PROJECT_DIR=/var/www/${PROJECT}

RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR

COPY requirements.txt .
RUN pip install -r requirements.txt

# Server
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]