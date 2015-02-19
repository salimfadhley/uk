#! /bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

if [ ! -d venv ]; then
    ./make_venv.sh
fi

source venv/bin/activate
cd $DIR/src
python setup.py develop
