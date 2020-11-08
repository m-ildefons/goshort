#!/bin/bash

RUN_SCRIPT="$0"
RUN_DIR=$(dirname "${RUNSCRIPT}")
VENV="${RUN_DIR}/venv"

if [ ! -d "${VENV}" ]; then
	python3 -m venv "${VENV}"
	source "${VENV}/bin/activate"
	python3 -m pip install -e .
else
	source "${VENV}/bin/activate"
fi

if [ ! -f "instance/goshort.sqlite" ]; then
	FLASK_APP="goshort" flask init-db
fi

if [ ! "${1}" == "init" ]; then
    waitress-serve --call 'goshort:create_app'
fi
