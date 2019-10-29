from veracode.API.core import REST

class SummaryReport(REST):
    def __init__(self):
        super(SummaryReport, self).__init__('summaryreport.do', 4.0)

    @classmethod
    def build(self, build_id):
        return self().GET({'build_id':build_id})


class SummaryReportPDF(REST):
    def __init__(self):
        super(SummaryReportPDF, self).__init__('summaryreportpdf.do', 4.0)

    @classmethod
    def build(self, build_id):
        return self().GET({'build_id':build_id}, format='content')


class DetailedReport(REST):
    def __init__(self):
        super(DetailedReport, self).__init__('detailedreport.do', 5.0)

    @classmethod
    def build(self, build_id):
        return self().GET({'build_id':build_id})


class DetailedReportPDF(REST):
    def __init__(self):
        super(DetailedReportPDF, self).__init__('detailedreportpdf.do', 4.0)

    @classmethod
    def build(self, build_id):
        return self().GET({'build_id':build_id}, format='content')


class ThirdPartyReportPDF(REST):
    def __init__(self):
        super(ThirdPartyReportPDF, self).__init__('thirdpartyreportpdf.do', 4.0)

    @classmethod
    def build(self, build_id):
        return self().GET({'build_id':build_id}, format='content')


class GetCallStacks(REST): # UNTESTED
    def __init__(self):
        super(GetCallStacks, self).__init__('getcallstacks.do', 5.0)

    @classmethod
    def get(self, build_id, flaw_id):
        return self().GET({'build_id':build_id, 'flaw_id':flaw_id})


class GetAppBuilds(REST):
    def __init__(self):
        super(GetAppBuilds, self).__init__('getappbuilds.do', 4.0)

    @classmethod
    def get(self, report_changed_since=None, only_latest=None, 
            include_in_progress=None):
        return self().GET({'report_changed_since':report_changed_since,
                           'only_latest':only_latest,
                           'include_in_progress':include_in_progress})


class GetAccountCustomFieldList(REST):
    def __init__(self):
        super(GetAccountCustomFieldList, self).__init__(
                'getaccountcustomfieldlist.do', 5.0)

    @classmethod
    def get(self):
        return self().GET()


