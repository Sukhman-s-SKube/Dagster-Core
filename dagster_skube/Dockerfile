FROM python:3.11-slim

ENV DAGSTER_HOME=/opt/dagster
WORKDIR ${DAGSTER_HOME}

RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
 && pip install \
      "dagster[postgres,aws]==1.*" \
      dagit==1.* \
      dagster-postgres

COPY . .

RUN pip install -e .

RUN useradd -U -m dagster
USER dagster

EXPOSE 3000

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["\
  case \"$DAGSTER_COMPONENT\" in \
    daemon) \
      exec dagster-daemon run \
      ;; \
    webserver|*) \
      exec dagster-webserver \
        -h 0.0.0.0 \
        -p 3000 \
      ;; \
  esac"]

