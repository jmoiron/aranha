#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Assorted utilities."""

import random
from aranha import VERSION

useragent = 'Aranha %s' % ('.'.join(map(str,VERSION)))

uas = (
    # webkit
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) '
        'AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.127 Safari/533.4',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) '
        'AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    # ffox
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    # ies
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; WOW64; SLCC1; .NET '
        'CLR 2.0.50727; .NET CLR 3.0.04506; .NET CLR 1.1.4322)',
)

def ua(random=False):
    if random:
        return random.choice(uas)
    return useragent

def queueitems(queue):
    l = []
    while not queue.empty():
        l.append(queue.get_nowait())
    return l

