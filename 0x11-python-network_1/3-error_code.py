#!/usr/bin/python3
import urllib.parse
import sys
import urllib.request

"""
hanldes error
"""

if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as responce:
            print(responce.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
