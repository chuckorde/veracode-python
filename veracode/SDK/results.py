from veracode.SDK.core import Parser
from veracode.SDK.exceptions import *
import veracode.API as API
from lxml import etree
import os

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


# results
class SummaryReport(BaseReport):
    def __init__(self, build_id):
        super(SummaryReport, self).__init__('SummaryReport',
                {'build_id': build_id})

class DetailedReport(BaseReport):
    def __init__(self, build_id):
        super(DetailedReport, self).__init__('DetailedReport',
                {'build_id': build_id})

class GetAccountCustomFieldList(BaseReport):
    def __init__(self):
        super(GetAccountCustomFieldList, self).__init__(
                'GetAccountCustomFieldList', fn='get')

class GetCallStacks(BaseReport):
    def __init__(self, build_id, flaw_id):
        super(GetCallStacks, self).__init__(
                'GetCallStacks',
                {'build_id':build_id, 'flaw_id':flaw_id}, fn='get')


# PDF reports
class SummaryReportPDF(BasePDF):
    def __init__(self, build_id):
        super(SummaryReportPDF, self).__init__('SummaryReportPDF',
                {'build_id': build_id})

class DetailedReportPDF(BasePDF):
    def __init__(self, build_id):
        super(DetailedReportPDF, self).__init__('DetailedReportPDF',
                {'build_id': build_id})

class ThirdPartyReportPDF(BasePDF):
    def __init__(self, build_id):
        super(ThirdPartyReportPDF, self).__init__('ThirdPartyReportPDF',
                {'build_id': build_id})


