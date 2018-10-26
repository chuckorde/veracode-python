import xmltodict
import strconv
import json, os
from lxml import etree
import veracode.API as API
from veracode.SDK.exceptions import *

class Struct(object):
    def __init__(self, attrs):
        for key in attrs.keys():
            try:
                attrs[key] = strconv.convert(attrs[key])
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

class BaseReport(Parser):
    def __init__(self, report, args=None, fn='build'):
        if args:
            res = getattr(getattr(API.results, report),fn)(**args)
        else:
            res = getattr(getattr(API.results, report),fn)()

        self.data = res.data
        self.status_code = res.status_code
        self._update_properties()

    def _update_properties(self):
        if self.status_code != 200:
            raise Exception(self.data)

        data = self._objectify(self._parse_xml(self.data))
        xml = etree.XML(bytes(self.data, 'utf-8'))
        root = etree.QName(xml.tag).localname
        if root == 'error':
            raise VeracodeInvalidArgumentError(xml.text)

        for k in getattr(data, root).__dict__.keys():
            setattr(self, k, getattr(getattr(data, root), k))

class BasePDF(object):
    def __init__(self, report, build_id):
        res = getattr(API.results, report).build(build_id)
        self.pdf = res.data
        self.status_code = res.status_code

    def save(self, path):
        with open(path, 'wb') as f:
            f.write(self.pdf)
        return self.status_code == 200
