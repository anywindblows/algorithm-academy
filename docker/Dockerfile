FROM python:3.11.3-slim as requirements-stage
ARG FASTAPI_ENV
ENV FASTAPI_ENV=${FASTAPI_ENV}
WORKDIR /tmp
RUN pip install poetry==1.7.1
COPY ./pyproject.toml ./poetry.lock* /tmp/
# hadolint ignore=SC2046
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes \
    $(if [ "$FASTAPI_ENV" = 'development' ]; then echo '--with dev'; fi)


FROM python:3.11.3-slim as development_build
# Needed for fixing permissions of files created by Docker:
ARG UID=1000
ARG GID=1000
ENV \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
  # Cleaning cache:
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*
WORKDIR /code
RUN groupadd -g "${GID}" -r web \
  && useradd -d '/code' -g web -l -r -u "${UID}" web \
  && chown web:web -R '/code'
# Project initialization:
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --verbose --no-cache-dir --upgrade -r /code/requirements.txt


# The following stage is only for production:
FROM development_build AS production_build
COPY --chown=web:web . /code
