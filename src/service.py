from .model import ResponseDao
from collections import OrderedDict


def reply(obj: OrderedDict) -> ResponseDao:
    message = 'Listening to {}; from Discovery, Over!'.format(obj['from'])
    return ResponseDao(to=obj['from'], message=message)
