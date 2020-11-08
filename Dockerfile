FROM python:3-slim as initializer

COPY run.sh /run.sh
COPY goshort /goshort
COPY setup.py /setup.py
COPY setup.cfg /setup.cfg

RUN /run.sh init

FROM python:3-slim

COPY --from=initializer /run.sh /run.sh
COPY --from=initializer /goshort /goshort
COPY --from=initializer /instance /instance
COPY --from=initializer /venv /venv

EXPOSE 8080/tcp

ENTRYPOINT ["/run.sh"]
