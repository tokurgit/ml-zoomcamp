FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

# Use model2 from base image
COPY ["score.py", "./"]

EXPOSE 1234

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:1234", "score:app", "--access-logfile=-" ]