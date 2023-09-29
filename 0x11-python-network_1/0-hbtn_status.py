#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


from urllib.request import urlopen
import json

with urlopen("https://alx-intranet.hbtn.io/status") as response:
    data = json.loads(response.read().decode())
    for key, value in data.items():
        print("\t- " + key + ": " + value)

