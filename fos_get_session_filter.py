import requests
import urllib3
import json
import sys

# Disable SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

### UPDATE FOR YOUR ENVIRONMENT ###
HOST_IP = "1.1.1.1"
API_TOKEN = "xxxxxxx"
##################################

BASE_URL = "https://" + HOST_IP + "/api/v2/"

HEADERS = {
    "Accept": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

def verify_login():
    '''
    Verifies the API token and host by calling a simple status endpoint.
    Returns True if valid, False otherwise.
    '''
    url = BASE_URL + "monitor/system/status"
    try:
        response = requests.get(url, headers=HEADERS, verify=False)
        if response.status_code == 200:
            print("Login successful.")
            return True
        else:
            print(f"Login failed: {response.status_code} - {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Request error during login verification: {e}")
        return False
    
def print_json(data):
    '''Pretty-print a dictionary or JSON-like object.'''
    print(json.dumps(data, indent=4))

def get_session_filter(filter=None):
    '''
    get sessions and filter 

    Args:
        none

    Returns:
        JSON response or none
    '''
    api_call = 'monitor/firewall/session?count=9999'
    
    if(filter):
        url = BASE_URL + api_call + "&" + filter
    else:
        url = BASE_URL + api_call

    try:
        response = requests.get(url, headers=HEADERS, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None





def main():
    ''' The main function/program '''
    if not verify_login():
        sys.exit("Login failed. Please check HOST_IP or API_TOKEN.")

    # Created a filter for destionation port 8922
    filter = "destport=8922"

    # If filter variable above not passed, will just get sessions with ?count=9999
    result = get_session_filter(filter)
    if result:
        print_json(result)

    
    ''' End main function/program '''

## Run the main function/program
if __name__ == '__main__':
    main()

