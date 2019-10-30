from veracode.API.core import REST

class ThirdPartyReportPDF(REST):
    """ class: veracode.API.results.ThirdPartyReportPDF
    
        params: dynamic, see veracode.SDK.results.ThirdPartyReportPDF for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(ThirdPartyReportPDF, self).__init__('thirdpartyreportpdf.do', 4.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class GetAccountCustomFieldList(REST):
    """ class: veracode.API.results.GetAccountCustomFieldList
    
        params: dynamic, see veracode.SDK.results.GetAccountCustomFieldList for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GetAccountCustomFieldList, self).__init__('getaccountcustomfieldlist.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class DetailedReport(REST):
    """ class: veracode.API.results.DetailedReport
    
        params: dynamic, see veracode.SDK.results.DetailedReport for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(DetailedReport, self).__init__('detailedreport.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class GetAppBuilds(REST):
    """ class: veracode.API.results.GetAppBuilds
    
        params: dynamic, see veracode.SDK.results.GetAppBuilds for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GetAppBuilds, self).__init__('getappbuilds.do', 4.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class SummaryReport(REST):
    """ class: veracode.API.results.SummaryReport
    
        params: dynamic, see veracode.SDK.results.SummaryReport for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(SummaryReport, self).__init__('summaryreport.do', 4.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class DetailedReportPDF(REST):
    """ class: veracode.API.results.DetailedReportPDF
    
        params: dynamic, see veracode.SDK.results.DetailedReportPDF for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(DetailedReportPDF, self).__init__('detailedreportpdf.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class SummaryReportPDF(REST):
    """ class: veracode.API.results.SummaryReportPDF
    
        params: dynamic, see veracode.SDK.results.SummaryReportPDF for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(SummaryReportPDF, self).__init__('summaryreportpdf.do', 4.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class GetCallStacks(REST):
    """ class: veracode.API.results.GetCallStacks
    
        params: dynamic, see veracode.SDK.results.GetCallStacks for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GetCallStacks, self).__init__('getcallstacks.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    