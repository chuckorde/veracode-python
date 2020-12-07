from veracode.API.core import REST

class GetMinigationInfo(REST):
    """ class: veracode.API.mitigation.GetMinigationInfo
    
        params: dynamic, see veracode.SDK.mitigation.GetMinigationInfo for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(GetMinigationInfo, self).__init__('getminigationinfo.do', None, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    