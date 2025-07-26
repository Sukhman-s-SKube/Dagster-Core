FROM python:3.11-slim

ENV DAGSTER_HOME=/opt/dagster
WORKDIR ${DAGSTER_HOME}

RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir \
      "dagster[postgres,aws]==1.*" \
      dagit==1.* \
      dagster-postgres

COPY . .

COPY dagster_skube/dagster.yaml ${DAGSTER_HOME}/dagster.yaml

RUN pip install --no-cache-dir -e ./dagster_skube

RUN mkdir -p ${DAGSTER_HOME}/history \
 && chown -R 1000:1000 ${DAGSTER_HOME}

RUN useradd -u 1000 -U -m dagster
USER dagster

EXPOSE 3000

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["\
case \"$DAGSTER_COMPONENT\" in \
  daemon)     exec dagster-daemon run ;; \
  webserver|*) exec dagster-webserver -h 0.0.0.0 -p 3000 ;; \
esac"]


