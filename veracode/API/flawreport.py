from veracode.API.core import REST

class GenerateFlawReport(REST):
    """ class: veracode.API.flawreport.GenerateFlawReport
    
        params: dynamic, see veracode.SDK.flawreport.GenerateFlawReport for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GenerateFlawReport, self).__init__('generateflawreport.do', 3.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    