#!/bin/bash
SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
cd $SHELL_FOLDER/..
if [ ! -d "venv" ]; then
  python -m venv .venv
fi
source .venv/bin/activate
pip install -r src/requirements.txt