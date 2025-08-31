#!/bin/bash
#Author: Rohtash Lakra
echo
#python -m unittest discover -s ./test/blueprints -p "test_affiliate_link.py"
python -m unittest discover -s ./test/ -p "test_*.py"
echo

