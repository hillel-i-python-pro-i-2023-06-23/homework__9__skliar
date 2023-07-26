FROM python:3.11

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./run.py run.py
COPY --chown=${USER} ./app app
#COPY --chown=${USER} ./data_base data_base
COPY --chown=${USER} ./templates templates

USER ${USER}

ENTRYPOINT ["python", "run.py"]