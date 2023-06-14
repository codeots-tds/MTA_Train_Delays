#!/bin/sh

here="$(cd "$(dirname "$0")" && pwd)"
set -x

cd "${here}"

if ! python3 -c 'import pipenv'
then
    echo "You don't have \`pipenv\`, so I'll install it for you"
    python3 -m pip install --user --no-input pipenv
fi

if ! [ -x $here/.venv/bin/python3 ]
then
   python3 -m pipenv install
fi

./.venv/bin/python3 app/main.py
