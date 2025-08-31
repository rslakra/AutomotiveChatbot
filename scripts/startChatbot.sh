#!/bin/bash
#Author: Rohtash Lakra
echo
echo "Arguments: $#"
echo
python app/main.py
#if [ $# -eq 0 ]; then
#    exec gunicorn --name "gunicorn" -c gunicorn-config.py wsgi:wsgi
#else
#    gunicorn --name "gunicorn" -c gunicorn-config.py wsgi:wsgi
#fi
echo
