#!/usr/bin/python3
"""
Add items
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except Exception:
    json_list = []
    json_list.append(sys.argv[i1:])
save_to_json_file(json_list, filename)
