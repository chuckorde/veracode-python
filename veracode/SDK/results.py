from veracode.SDK.core import Base, BasePDF

class SummaryReport(Base):
    def __init__(self, build_id):
        super(SummaryReport, self).__init__(
                module='results', 
                cls='SummaryReport', 
                fn='build',
                args={'build_id': build_id})

class DetailedReport(Base):
    def __init__(self, build_id):
        super(DetailedReport, self).__init__(
                module='results', 
                cls='DetailedReport',
                fn='build', 
                args={'build_id': build_id})

class GetAccountCustomFieldList(Base):
    def __init__(self):
        super(GetAccountCustomFieldList, self).__init__(
                module='results', 
                cls='GetAccountCustomFieldList',
                fn='get')

class GetCallStacks(Base):
    def __init__(self, build_id, flaw_id):
        super(GetCallStacks, self).__init__(
                module='results', 
                cls='GetCallStacks', 
                fn='get',
                args={'build_id':build_id, 'flaw_id':flaw_id})

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


