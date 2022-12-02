import time
from flask import url_for

def my_url_for(endpoint, **values):
    url = url_for(endpoint, **values)
    return url + '?ts={}'.format(int(time.time()))