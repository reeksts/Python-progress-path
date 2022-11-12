# This is a tutorial following:
# https://www.youtube.com/watch?v=1lxrb_ezP-g&t=1426s

import requests
import json

url = 'https://formulae.brew.sh/api/formula.json'

r = requests.get(url)
packages_json = r.json()

paskages_str = json.dumps(packages_json, indent=2)

print(paskages_str)