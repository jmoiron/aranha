#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Aranha job encapsulation."""

import utils

class Job(object):
    """Encapsulation of a job to put in the job queue.  Contains at least
    a URL, but can also have custom headers or entirely custom meta
    information.  The response object and data are tacked onto this object,
    which is then returned to the handler for processing."""
    default_headers = {
        'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;',
        'Accept-Encoding': 'gzip,deflate',
        'Cache-Control': 'max-age=0',
    }
    def __init__(self, url, headers=None, meta=None, method='GET', handler=None,
            body=None, randomua=False):
        self.__url = url
        self.method = method
        self.headers = dict(self.default_headers)
        self.headers.update(headers or {})
        self.headers['User-Agent'] = utils.ua(randomua)
        self.body = body
        self.meta = meta
        self.handler = handler

    def __hash__(self):
        return hash(self.url)

    def __cmp__(self, other):
        return cmp(hash(self), hash(other))

    def __repr__(self):
        return '<Job: %s (%s)>' % (
            self.url,
            'done: %d' % len(self.data) if hasattr(self, 'data') else 'pending',
        )

    url = property(lambda self: self.__url)

