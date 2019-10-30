from veracode.API.core import REST

class UpdateSandbox(REST):
    """ class: veracode.API.sandbox.UpdateSandbox
    
        params: dynamic, see veracode.SDK.sandbox.UpdateSandbox for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(UpdateSandbox, self).__init__('updatesandbox.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class CreateSandbox(REST):
    """ class: veracode.API.sandbox.CreateSandbox
    
        params: dynamic, see veracode.SDK.sandbox.CreateSandbox for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(CreateSandbox, self).__init__('createsandbox.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class getSandboxList(REST):
    """ class: veracode.API.sandbox.getSandboxList
    
        params: dynamic, see veracode.SDK.sandbox.getSandboxList for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(getSandboxList, self).__init__('getsandboxlist.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class PromoteSandbox(REST):
    """ class: veracode.API.sandbox.PromoteSandbox
    
        params: dynamic, see veracode.SDK.sandbox.PromoteSandbox for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(PromoteSandbox, self).__init__('promotesandbox.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    