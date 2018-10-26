from veracode.API.core import REST

class GetAppList(REST):
    def __init__(self):
        super(GetAppList, self).__init__('getapplist.do', 5.0)

    @classmethod
    def get(self, include_user_info=None):
        return self().GET({'include_user_info':include_user_info})


class GetAppInfo(REST):
    def __init__(self):
        super(GetAppInfo, self).__init__('getappinfo.do', 5.0)

    @classmethod
    def get(self, app_id):

        return self().GET({'app_id':app_id})


class GetBuildInfo(REST):
    def __init__(self):
        super(GetBuildInfo, self).__init__('getbuildinfo.do', 5.0)

    @classmethod
    def get(self, app_id, build_id=None, sandbox_id=None):
        return self().GET({'app_id':app_id, 'build_id':build_id,
                           'sandbox_id':sandbox_id})


class GetBuildList(REST):
    def __init__(self):
        super(GetBuildList, self).__init__('getbuildlist.do', 5.0)

    @classmethod
    def get(self, app_id, sandbox_id=None):
        return self().GET({'app_id':app_id, 'sandbox_id':sandbox_id})


class GetFileList(REST):
    def __init__(self):
        super(GetFileList, self).__init__('getfilelist.do', 5.0)

    @classmethod
    def get(self, app_id, build_id=None, sandbox_id=None):
        return self().GET({'app_id':app_id, 'build_id':build_id,
                           'sandbox_id':sandbox_id})


class GetPolicyList(REST):
    def __init__(self):
        super(GetPolicyList, self).__init__('getpolicylist.do', 5.0)

    @classmethod
    def get(self, app_id, build_id=None, sandbox_id=None):
        return self().GET({'app_id':app_id, 'build_id':build_id,
                           'sandbox_id':sandbox_id})


class GetPreScanResults(REST):
    def __init__(self):
        super(GetPreScanResults, self).__init__('getprescanresults.do', 5.0)

    @classmethod
    def get(self, app_id, build_id=None, sandbox_id=None):
        return self().GET({'app_id':app_id, 'build_id':build_id,
                           'sandbox_id':sandbox_id})


class GetVendorList(REST):
    def __init__(self):
        super(GetVendorList, self).__init__('getvendorlist.do', 5.0)

    @classmethod
    def get(self, app_id, file_id=None, sandbox_id=None):
        return self().GET({'app_id':app_id, 'file_id':file_id,
                           'sandbox_id':sandbox_id})


