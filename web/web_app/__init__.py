from json import JSONDecodeError

import requests

EXP_URL = 'http://exp-api:8000/'


def make_path(paths):
    return EXP_URL + ('{}/' * len(paths)).format(*paths)


def get(*paths, params=None):
    """
    Performs a get request on the experience API layer.
    For example, get('hello', 'world') will query http://exp-api:8000/hello/world
    :param paths: each sub-path entered as a separate argument
    :param params: URL parameters
    :return: JSON response from experience API
    """
    try:
        return requests.get(make_path(paths), params=params).json()
    except JSONDecodeError:
        return {}


def post(*paths, data=None):
    return requests.post(make_path(paths), data=data)


def fill_defaults(target, defaults):
    acc = {k: v for k, v in target.items()}
    for k in filter(lambda k: k not in target, defaults):
        acc[k] = defaults[k]
    return acc
