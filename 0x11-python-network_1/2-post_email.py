#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter,"""
import urllib.parse
import sys
import urllib.request


if __name__ == "__main__":
    post_dict = {"email": sys.argv[2]}
    url_encoded_data = urllib.parse.urlencode(post_dict)
    with urllib.request.urlopen(sys.argv[1], data=url_encoded_data.encode("utf-8")) as response:
        print(f"Your email is: {response.getheader('email')}")
