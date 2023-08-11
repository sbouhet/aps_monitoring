#!/bin/bash
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
vars=$SCRIPTPATH"/export-vars.sh"
source $vars
cmd="/usr/bin/python "$SCRIPTPATH"/main.py --action check --username "$APSYSTEMS_USER" --pwd "$APSYSTEMS_PWD" --key "$PUSHSAFER_KEY
$cmd
