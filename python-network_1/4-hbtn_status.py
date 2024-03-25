#!/usr/bin/python3
"""__summary__
- python scripts that fetches https://alu-intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    if url.startswith('https://'):
        url = "https://alu-intranet.hbtn.io/status"
        
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
