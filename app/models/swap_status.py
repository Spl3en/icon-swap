import requests
import certifi
import json

def create_jsonrpc_request_content (method, params):
    content = {
        'jsonrpc': '2.0',
        'method': method,
        'id': 1
    }
    if params is not None:
        content['params'] = params
    return content

def post (url, payload):
    try:
        path = certifi.where()
        r = requests.post (url, json=payload, verify=path)
        return r
    except requests.exceptions.Timeout:
        raise RuntimeError ("Timeout happened. Check your internet connection status.")

def get_status (address):

    if address == "0000000000000000000000000000000000000000":
        return True
    
    request = create_jsonrpc_request_content (
        "eth_call", [
            {
                "data" : "0xcb7bba39000000000000000000000000%s" % address, 
                "to" : "0xb5a5f22694352c15b00323844ad545abb2b11028"
            },
            "latest"
        ]
    )

    response = post ("https://node3.web3api.com/", request)
    data = json.loads (response.text)

    if int(data["result"], 16) == 1: # locked!
        return True

    return False