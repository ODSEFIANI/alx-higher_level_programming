#!/bin/bash
# Displays ALL THE HTTP methodds teh server accepts
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
