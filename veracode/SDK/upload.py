from veracode.SDK.core import Base

class GetAppInfo(Base):
    def __init__(self, app_id):
        super(GetAppInfo, self).__init__(
                module='upload',
                cls='GetAppInfo',
                fn='get',
                args={'app_id':app_id})


class GetAppList(Base):
    def __init__(self, include_user_info=None):
        super(GetAppList, self).__init__(
                module='upload',
                cls='GetAppList',
                fn='get',
                args={'include_user_info': include_user_info})


class GetBuildInfo(Base):
    def __init__(self, app_id, build_id=None, sandbox_id=None):
        super(GetBuildInfo, self).__init__(
                module='upload',
                cls='GetBuildInfo',
                fn='get',
                args={'app_id':app_id, 'build_id':build_id,
                      'sandbox_id':sandbox_id})


class GetBuildList(Base):
    def __init__(self, app_id, sandbox_id=None):
        super(GetBuildList, self).__init__(
                module='upload',
                cls='GetBuildList',
                fn='get',
                args={'app_id':app_id, 'sandbox_id':sandbox_id})


class GetFileList(Base):
    def __init__(self, app_id, build_id=None, sandbox_id=None):
        super(GetFileList, self).__init__(
                module='upload',
                cls='GetFileList',
                fn='get',
                args={'app_id':app_id, 'build_id':build_id,
                      'sandbox_id':sandbox_id})


class GetPolicyList(Base):
    def __init__(self, app_id, build_id=None, sandbox_id=None):
        super(GetPolicyList, self).__init__(
                module='upload',
                cls='GetPolicyList',
                fn='get',
                args={'app_id':app_id, 'build_id':build_id,
                      'sandbox_id':sandbox_id})


class GetPreScanResults(Base):
    def __init__(self, app_id, build_id=None, sandbox_id=None):
        super(GetPreScanResults, self).__init__(
                module='upload',
                cls='GetPreScanResults',
                fn='get',
                args={'app_id':app_id, 'build_id':build_id,
                      'sandbox_id':sandbox_id})


class GetVendorList(Base):
    def __init__(self, app_id, file_id, sandbox_id=None):
        super(GetPreScanResults, self).__init__(
                module='upload',
                cls='GetVendorList',
                fn='get',
                args={'app_id':app_id, 'file_id':file_ide,
                      'sandbox_id':sandbox_id})

