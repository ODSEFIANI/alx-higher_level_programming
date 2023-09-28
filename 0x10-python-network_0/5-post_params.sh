#!/bin/bash
# SEND POST request and displays the bodey of the responce
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
