#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Handler classes designed to work with the crawler."""

class BaseHandler(object):
    """Base handler object that does nothing."""

    def preprocess(self, job):
        pass

    def postprocess(self, job):
        pass

class SimpleHandler(BaseHandler):
    """A simple handler that takes pre and post processing methods as
    arguments.  The crawler will be passed to these callbacks as a crawler
    kwarg."""
    def __init__(self, preprocess=None, postprocess=None):
        self.pre = preprocess
        self.post = postprocess
        super(SimpleHandler, self).__init__()

    def preprocess(self, job):
        if self.pre:
            self.pre(job, crawler=self.crawler)

    def postprocess(self, job):
        if self.post:
            self.post(job, crawler=self.crawler)

