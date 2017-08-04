#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 17/04/2014

@author: jeanmachuca
'''

class uXMLException(Exception):
    pass

UXMLOBJ_ENABLED = False
try:
    import cElementTree as ET
except ImportError:
    try:
        import xml.etree.cElementTree as ET
    except ImportError, (ex):
        raise uXMLException(str(ex))

try:
    import urllib2
    UXMLOBJ_ENABLED = True
except ImportError, (ex):
    raise uXMLException(str(ex))

class uXML2Object(object):
    obj = {}
    childParents = []
    root = None
    tag = None
    attrs = []
    url = ''
    _xmlns = ''

    def __init__(self,url,_xmlns,root=None):
        self.url = url
        dom = ET.parse(urllib2.urlopen(url))
        self.xmlns = _xmlns
        if root is None:
            self.root = dom.getroot()
        else:
            self.root = root
        self.process()

    def xmlns(): #@NoSelf
        def fget(self):
            return '{%s}' % self._xmlns

        def fset(self, value):
            self._xmlns = value

        def fdel(self):
            del self._xmlns

        return locals()

    xmlns = property(**xmlns())


    def iterparent(self,tree):
        for parent in tree.getiterator():
            for child in parent:
                yield parent, child

    def process(self):
        for parent, child in self.iterparent(self.root):
            self.childParents.append({'element':child,'parent':parent})
            if not self.obj.__contains__(parent.tag):
                self.obj[parent.tag]  = {}
            self.obj[parent.tag][child.tag] = child

    def _query_tag_name(self,tag):
        return tag

    def _tag_name(self,tag):
        return r'%s%s' % (self.xmlns,self._query_tag_name(tag))

    def find(self,query):
        tags = [self._tag_name(tag) for tag in query.split(' ')]
        obj = self.obj
        _found = True
        for _tag in tags:
            try:
                if (not obj is None) and obj.__contains__(_tag):
                    obj = obj[_tag]
                else:
                    _found = False
            except:
                obj = filter(lambda o: True if o.tag.__eq__(self._tag_name(_tag)) else False,obj)
                pass
        return obj if _found else None
