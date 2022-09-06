#!/bin/bash
SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
cd $SHELL_FOLDER/..
source .venv/bin/activate
pip freeze > src/requirements.txt
