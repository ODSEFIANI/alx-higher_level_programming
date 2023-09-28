#!/bin/bash
# displays the status code if the responce
curl -s -L -I "$1" -o /dev/null -w '%{http_code}'
