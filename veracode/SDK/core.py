import xmltodict
import strconv
import json

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
