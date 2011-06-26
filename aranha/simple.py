#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A simple interface to the base crawler and handlers that allows for natural
script-style usage of the spider.  The goal here is to provide convenience
functions to scale down the spidering task to the definition of a few callbacks
and the call of a function."""

import urllib

from aranha.utils import queueitems

from aranha.job import Job
from aranha.handler import BaseHandler, SimpleHandler
from aranha.crawler import Crawler

def job_from_request(request):
    """Create a job from a urllib2.Request object."""
    url = request.get_full_url()
    headers = dict(request.headers)
    method = request.get_method()
    body = request.data
    if isinstance(body, dict):
        body = urllib.urlencode(body)
    return Job(url, headers=headers, method=method, body=body)

def starturls(urls, callback, concurrency=4, timeout=2):
    """Fetch a number of urls.  These may be string urls or jobs."""
    handler = SimpleHandler(preprocess=callback)
    jobs = [Job(url, handler=handler) for url in urls]
    fetchjobs(jobs, concurrency, timeout, handler=handler)

def startjobs(jobs, concurrency=4, timeout=2, handler=None):
    """Fetch a number of jobs.  These jobs should have handlers set, as the
    BaseHandler with noop callbacks will be used."""
    handler = handler or BaseHandler()
    handler.jobs = jobs
    crawler = Crawler(handler, concurrency=concurrency, timeout=timeout)
    crawler.start()

def geturls(urls, concurrency=4, timeout=5):
    """Get a list of urls.  This synchronous call fetches all urls
    asynchronously and returns the data within."""
    from gevent import queue
    q = queue.Queue()
    def callback(job, crawler):
        q.put({'url': job.url, 'document': job.data})
    handler = SimpleHandler(preprocess=callback)
    jobs = [Job(url, handler=handler) for url in urls]
    handler.jobs = jobs
    crawler = Crawler(handler, concurrency=concurrency, timeout=timeout)
    crawler.start()
    return queueitems(q)

