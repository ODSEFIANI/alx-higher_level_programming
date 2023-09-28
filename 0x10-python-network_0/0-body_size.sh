#!/bin/bash
# Get the byte size of the HTTP responceL.
curl -s "$1" | wc -c
