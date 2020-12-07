from veracode.API.core import REST

class DeleteUser(REST):
    """ class: veracode.API.admin.DeleteUser
    
        params: dynamic, see veracode.SDK.admin.DeleteUser for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(DeleteUser, self).__init__('deleteuser.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class UpdateUser(REST):
    """ class: veracode.API.admin.UpdateUser
    
        params: dynamic, see veracode.SDK.admin.UpdateUser for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(UpdateUser, self).__init__('updateuser.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class GetTrackList(REST):
    """ class: veracode.API.admin.GetTrackList
    
        params: dynamic, see veracode.SDK.admin.GetTrackList for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(GetTrackList, self).__init__('gettracklist.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class GetMaintenanceScheduleInfo(REST):
    """ class: veracode.API.admin.GetMaintenanceScheduleInfo
    
        params: dynamic, see veracode.SDK.admin.GetMaintenanceScheduleInfo for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(GetMaintenanceScheduleInfo, self).__init__('getmaintenancescheduleinfo.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class GetTeamList(REST):
    """ class: veracode.API.admin.GetTeamList
    
        params: dynamic, see veracode.SDK.admin.GetTeamList for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(GetTeamList, self).__init__('getteamlist.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class GetUserInfo(REST):
    """ class: veracode.API.admin.GetUserInfo
    
        params: dynamic, see veracode.SDK.admin.GetUserInfo for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(GetUserInfo, self).__init__('getuserinfo.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class DeleteTeam(REST):
    """ class: veracode.API.admin.DeleteTeam
    
        params: dynamic, see veracode.SDK.admin.DeleteTeam for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(DeleteTeam, self).__init__('deleteteam.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class CreateUser(REST):
    """ class: veracode.API.admin.CreateUser
    
        params: dynamic, see veracode.SDK.admin.CreateUser for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(CreateUser, self).__init__('createuser.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class GetUserList(REST):
    """ class: veracode.API.admin.GetUserList
    
        params: dynamic, see veracode.SDK.admin.GetUserList for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(GetUserList, self).__init__('getuserlist.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class GetTeamInfo(REST):
    """ class: veracode.API.admin.GetTeamInfo
    
        params: dynamic, see veracode.SDK.admin.GetTeamInfo for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(GetTeamInfo, self).__init__('getteaminfo.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class GetCurricumList(REST):
    """ class: veracode.API.admin.GetCurricumList
    
        params: dynamic, see veracode.SDK.admin.GetCurricumList for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(GetCurricumList, self).__init__('getcurricumlist.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class CreateTeam(REST):
    """ class: veracode.API.admin.CreateTeam
    
        params: dynamic, see veracode.SDK.admin.CreateTeam for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(CreateTeam, self).__init__('createteam.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    
class UpdateTeam(REST):
    """ class: veracode.API.admin.UpdateTeam
    
        params: dynamic, see veracode.SDK.admin.UpdateTeam for more info
        
        returns: XML data from veracode API
    """
    def __init__(self, **kwargs):
        super(UpdateTeam, self).__init__('updateteam.do', 3.0, **kwargs)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')
        
    