FROM python:3.7

# python envs
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# python dependencies
COPY ./requirements/dev.txt /requirements/
COPY ./requirements/common.txt /requirements/
RUN pip install -r ./requirements/dev.txt

# upload scripts
COPY ./scripts/entrypoint.sh ./scripts/start.sh ./scripts/gunicorn.sh /

WORKDIR /app
