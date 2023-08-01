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
COPY --chown=${USER} ./templates templates

USER ${USER}

# создаю и говорю что это моя рабочая директория для БД, шоб она создавалась только внутри контейнера, БД хранится до тех пор, пока открыт контейнер, потом удаляется
#RUN mkdir -p /wd/data_base

#WORKDIR /wd

ENTRYPOINT ["python", "run.py"]