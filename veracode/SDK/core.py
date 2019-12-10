import xmltodict
import strconv
import json, os
import veracode.API as API
from veracode.SDK.exceptions import *

# I don't love the layout of this API.
# There's a lot of cruft here to get it into a useble form.

class Struct(object):
    def __init__(self, attrs):
        for key in attrs.keys():
            try:
                attrs[key] = strconv.convert(attrs[key])
            except: pass
            try:
                if key.endswith('s'):
                    if ',' in attrs[key]:
                        attrs[key] = attrs[key].split(',')
            except: pass
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
        res = getattr(getattr(getattr(API, module),cls),fn)(**args)
        self.data = res.data
        self.status_code = res.status_code
        self.__res = res.res
        self._update_properties()

    def _update_properties(self):
        if self.status_code != 200:
            self.__res.raise_for_status()

        data = self._objectify(self._parse_xml(self.data))
        tag, value = list(data.__dict__.items())[0]
        if tag == 'error':
            raise VeracodeInvalidArgumentError(value)

        for k in getattr(data, tag).__dict__.keys():
            setattr(self, k, getattr(getattr(data, tag), k))

class BasePDF(object):
    def __init__(self, cls, build_id):
        res = getattr(API.results, cls).build(build_id)
        self.pdf = res.data
        self.status_code = res.status_code

    def save(self, path):
        with open(path, 'wb') as f:
            f.write(self.pdf)
        return self.status_code == 200
