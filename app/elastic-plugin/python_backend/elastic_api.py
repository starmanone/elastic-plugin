import requests
import json

def get_search(url, params):
    
    # set headers
    headers = {'Content-type': 'application/json'}
    
    # load params from json
    params = json.loads(params)
    
    # sending get request and saving the response as response object
    response = requests.get(url=url, json=params, headers=headers)

    # extracting data in json format
    data = response.json()

    return data['hits']['hits']
