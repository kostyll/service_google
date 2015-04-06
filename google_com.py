#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import collections
import urllib
import urllib2
import urlparse
import xml.etree.ElementTree
import bs4

import service_api

class GOOGLE_CACHE(service_api.SynchronizedBaseAPI):
    """

    This service checks if the page with some url exists in Google Cache.
    If does, it will return the page content.

    You can access the cached version for any page that has been saved by Google with this:

    http://webcache.googleusercontent.com/search?q=cache:http://example.com/
    """
    cache_url = 'http://webcache.googleusercontent.com/search?q=cache:http://example.com/'

    def method_get_cached_page_by_url(self,url):
        """
        Retrives url from Google cache
        """
        url = self.cache_url+url

        page = urllib2.urlopen(url)

        if page.code != 200:
            return None

        return page

    @classmethod
    def represent(some_class):
        return "GOOGLE_CACHE"



__all__ = []

def register():
    return [GOOGLE_CACHE]
