#!/bin/sh

gunicorn serve:serve -b 0.0.0.0:8080