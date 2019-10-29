import xmltodict
import strconv
import json, os, re
import inspect
from functools import wraps
from lxml import etree

import veracode
import veracode.API as API
from veracode.SDK.exceptions import *


def flatten_if_list(obj):
    if isinstance(obj, list):
        return ','.join([str(o) if obj else '' for o in obj])
    return obj


def function_from_class_name(s):
    return re.sub('([a-z])([A-Z])', r'\1 \2', s).split()[::-1].pop().lower()


class Struct(object):
    def __init__(self, attrs):
        for key in attrs.keys():
            try:
                attrs[key] = strconv.convert(attrs[key])
            except:
                pass
            try:
                if key.endswith('s'):
                    if ',' in attrs[key]:
                        attrs[key] = attrs[key].split(',')
                    else:
                        attrs[key] = [attrs[key]]
            except:
                pass
        self.__dict__.update(**attrs)

class Parser(object):
    @classmethod
    def _parse_xml(self, data):
        return json.loads(json.dumps(xmltodict.parse(
                    data, attr_prefix='', cdata_key='')))

    @classmethod
    def _objectify(self, obj):
        if isinstance(obj, dict):
            return Struct({
                k.replace('-','_').replace(':','_'): 
                    self._objectify(v) for k,v in obj.items()})
        if isinstance(obj, list):
            return [self._objectify(o) for o in obj]
        return obj

class Base(Parser):
    def __init__(self, module, cls, fn, args=None):
        if args:
            # do list stuff
            res = getattr(getattr(getattr(API, module),cls),fn)(**args)
        else:
            res = getattr(getattr(getattr(API, module),cls),fn)()

        self.data = res.data
        self.status_code = res.status_code
        self.__res = res.res
        self._update_properties()

    def _update_properties(self):
        if self.status_code != 200:
            self.__res.raise_for_status()

        data = self._objectify(self._parse_xml(self.data))
        xml = etree.XML(bytes(self.data, 'utf-8'))
        root = etree.QName(xml.tag).localname
        if root == 'error':
            raise VeracodeInvalidArgumentError(xml.text)

        for k in getattr(data, root).__dict__.keys():
            setattr(self, k, getattr(getattr(data, root), k))

    def reflect(self, obj, name, frame):
        module = name.split('.').pop()
        cls = obj.__class__.__name__
        fn = function_from_class_name(obj.__class__.__name__)
        obj = getattr(getattr(veracode.SDK, module), cls)
        _,_,_,args = inspect.getargvalues(frame) 
        args = {
                k:v for (k,v) in args.items() 
                if (k != 'self' and k != '__class__' and not k.startswith('_'))
                }
        return (module, cls, fn, obj, args)


class BasePDF(object):
    def __init__(self, cls, build_id):
        res = getattr(API.results, cls).build(build_id)
        self.pdf = res.data
        self.status_code = res.status_code

    def save(self, path):
        with open(path, 'wb') as f:
            f.write(self.pdf)
        return self.status_code == 200

