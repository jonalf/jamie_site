#!/bin/bash

SITE_PATH=/var/www/html/test/test/

cp app.py ${SITE_PATH}__init__.py
cp -r static $SITE_PATH
cp -r templates $SITE_PATH
