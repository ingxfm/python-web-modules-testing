# Python Standard libraries

# 3rd-party libraries
import requests

# Local libraries

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

#print(type(res))

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

print(res.text[:262])
