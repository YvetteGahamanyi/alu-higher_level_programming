#!/usr/bin/python3
"""__summary__
- python scripts that fetches https://intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    if response.status_code == 200:
        print("\t- content: OK")
    else:
        print("\t- content: Unexpected status code: {}".format(response.status_code))
