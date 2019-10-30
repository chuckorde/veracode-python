from veracode.SDK.core import Base

class ThirdPartyReportPDF(Base):
    """ class: veracode.SDK.results.ThirdPartyReportPDF
    
        params: 
			build_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				build_id,
        ):
        
        super(ThirdPartyReportPDF, self).__init__(
            module='results',
            cls='ThirdPartyReportPDF',
            fn='get', 
            args={
				'build_id':build_id,
            })
    
class GetAccountCustomFieldList(Base):
    """ class: veracode.SDK.results.GetAccountCustomFieldList
    
        params: 


        returns: A python object that represents the returned API data.
    """
    def __init__(self,

        ):
        
        super(GetAccountCustomFieldList, self).__init__(
            module='results',
            cls='GetAccountCustomFieldList',
            fn='get', 
            args={

            })
    
class DetailedReport(Base):
    """ class: veracode.SDK.results.DetailedReport
    
        params: 
			build_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				build_id,
        ):
        
        super(DetailedReport, self).__init__(
            module='results',
            cls='DetailedReport',
            fn='get', 
            args={
				'build_id':build_id,
            })
    
class GetAppBuilds(Base):
    """ class: veracode.SDK.results.GetAppBuilds
    
        params: 
			report_changed_since: optional
			only_latest: optional
			include_in_progress: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				report_changed_since=None,
				only_latest=None,
				include_in_progress=None,
        ):
        
        super(GetAppBuilds, self).__init__(
            module='results',
            cls='GetAppBuilds',
            fn='get', 
            args={
				'report_changed_since':report_changed_since,
				'only_latest':only_latest,
				'include_in_progress':include_in_progress,
            })
    
class SummaryReport(Base):
    """ class: veracode.SDK.results.SummaryReport
    
        params: 
			build_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				build_id,
        ):
        
        super(SummaryReport, self).__init__(
            module='results',
            cls='SummaryReport',
            fn='get', 
            args={
				'build_id':build_id,
            })
    
class DetailedReportPDF(Base):
    """ class: veracode.SDK.results.DetailedReportPDF
    
        params: 
			build_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				build_id,
        ):
        
        super(DetailedReportPDF, self).__init__(
            module='results',
            cls='DetailedReportPDF',
            fn='get', 
            args={
				'build_id':build_id,
            })
    
class SummaryReportPDF(Base):
    """ class: veracode.SDK.results.SummaryReportPDF
    
        params: 
			build_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				build_id,
        ):
        
        super(SummaryReportPDF, self).__init__(
            module='results',
            cls='SummaryReportPDF',
            fn='get', 
            args={
				'build_id':build_id,
            })
    
class GetCallStacks(Base):
    """ class: veracode.SDK.results.GetCallStacks
    
        params: 
			flaw_id: required
			build_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				flaw_id,
				build_id,
        ):
        
        super(GetCallStacks, self).__init__(
            module='results',
            cls='GetCallStacks',
            fn='get', 
            args={
				'flaw_id':flaw_id,
				'build_id':build_id,
            })
    