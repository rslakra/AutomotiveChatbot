#!/bin/bash
#Author: Rohtash Lakra
echo
gunicorn -c gunicorn_config.py wsgi:wsgi
echo
