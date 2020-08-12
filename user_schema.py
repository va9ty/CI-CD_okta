import json
import requests
from datetime import datetime


def main(Okta_tenant, API_token):
	url = Okta_tenant+"/api/v1/meta/schemas/user/default"
	header = {
	    'authorization': 'SSWS '+API_token,
	    'content-type': 'application/json'

	    }

	response_staged = requests.get(url, headers=header)
	user_schema = json.loads(response_staged.text)
	#print(user_schema)
	properties = user_schema["definitions"]["base"]["properties"]
	property_keys = list(properties.keys())

	return property_keys

