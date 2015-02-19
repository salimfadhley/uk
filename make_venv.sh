#! /bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
virtualenv $DIR/venv --python=`which python2` --prompt="(pythonjobs)"
