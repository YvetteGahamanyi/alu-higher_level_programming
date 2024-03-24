#!/usr/bin/python3
"""__summary__
- takes in a URL
- sends a request to the URL and displays the body of the response (decoded in utf-8).
- error management
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
