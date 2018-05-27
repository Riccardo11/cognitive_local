# coding: utf-8
# import json
# import urllib
# import logging

# from google.appengine.api import urlfetch
import requests


def call_vision_api(url):
    request = {
            "requests": [
                {
                "image": {
                    "source": {
                        "imageUri": url
                        }
                },
                "features": [
                    {
                    "type": "LOGO_DETECTION",
                    "maxResults": 1
                    }
                ]
                }
            ]
            }

    # try:
    #     result = urlfetch.fetch(
    #         url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyAu3mTFbbDfhiXX-rehjnA7eQjnq5EAwys',
    #         payload=json.dumps(request),
    #         method=urlfetch.POST,
    #         headers={'Content-Type': 'application/json'})
    #     return json.loads(result.content)
    # except urlfetch.Error:
    #     logging.exception('Caught exception fetching url')

    r = requests.post(
        'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyAu3mTFbbDfhiXX-rehjnA7eQjnq5EAwys',
        data = request,
        headers = {'Content-Type': 'application/json'}
        )

    return r.text