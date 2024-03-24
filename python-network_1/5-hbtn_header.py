#!/usr/bin/python3
"""__summary__
- takes in a URL
- sends a request to the URL 
- and displays the value of the variable X-Request-Id.
"""

import sys
import requests

if __name__ == '__main__':
    reqs = requests.get(sys.argv[1])
    print(reqs.headers.get("X-Request-Id"))
