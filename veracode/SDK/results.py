from veracode.SDK.core import BaseReport, BasePDF

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


