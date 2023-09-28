#!/bin/bash
# Send GET request with A header variable X-School-User-Id
curl -sH "X-School-User-Id: 98" "$1"
