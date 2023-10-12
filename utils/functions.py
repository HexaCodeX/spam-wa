import requests
from lib.Config import Config
from urllib.parse import urlparse
from utils.io import log
from utils.colors import yellow, white, purple

default_response = requests.get("https://google.com")

def is_production ():
    return Config.environment == "production"

def xhr (method, url, headers = None, data = None, proxies=None, json=None, files=None, timeout=3):
    func = getattr(requests, method)
    meta_URL = urlparse(url)
    response = None
    # log("info", f"waiting response '{ url }' with method [{yellow}{ method }{white}]")
    
    try:
        response = func(url, headers=headers, data=data, proxies=proxies, json=json, files=files, timeout=timeout)
        log("info", f"| response | [{yellow}{ method.upper() }{white}] [{purple}{response.status_code}{white}] | { meta_URL.hostname } |")
        
    except Exception as error:
        if not is_production():
            log("danger", f"error occured on '{ url }' with method [{yellow}{ method.upper() }{white}]")
            
        return default_response
        # raise Exception( f"error occured on '{ url }' with method [{ method }]")
    
    return response