#!/usr/bin/python3
"""__summary__
- takes in a URL and email
- sends a POST request to the passed URL with the email
- as a parameter displays the body of the response (decoded in utf-8)
"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    reqs = requests.post(url, data=value)
    print(reqs.text)
