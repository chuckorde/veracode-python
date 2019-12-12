from veracode.API.core import REST

class GetAppList(REST):
    """ class: veracode.API.upload.GetAppList

        params: dynamic, see veracode.SDK.upload.GetAppList for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GetAppList, self).__init__('getapplist.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class UpdateBuild(REST):
    """ class: veracode.API.upload.UpdateBuild

        params: dynamic, see veracode.SDK.upload.UpdateBuild for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(UpdateBuild, self).__init__('updatebuild.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class DeleteBuild(REST):
    """ class: veracode.API.upload.DeleteBuild

        params: dynamic, see veracode.SDK.upload.DeleteBuild for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(DeleteBuild, self).__init__('deletebuild.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class GetBuildInfo(REST):
    """ class: veracode.API.upload.GetBuildInfo

        params: dynamic, see veracode.SDK.upload.GetBuildInfo for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GetBuildInfo, self).__init__('getbuildinfo.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class GetAppInfo(REST):
    """ class: veracode.API.upload.GetAppInfo

        params: dynamic, see veracode.SDK.upload.GetAppInfo for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GetAppInfo, self).__init__('getappinfo.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class GetPolicyList(REST):
    """ class: veracode.API.upload.GetPolicyList

        params: dynamic, see veracode.SDK.upload.GetPolicyList for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GetPolicyList, self).__init__('getpolicylist.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class BeginPrescan(REST):
    """ class: veracode.API.upload.BeginPrescan

        params: dynamic, see veracode.SDK.upload.BeginPrescan for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(BeginPrescan, self).__init__('beginprescan.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class UploadLargeFile(REST):
    """ class: veracode.API.upload.UploadLargeFile

        params: dynamic, see veracode.SDK.upload.UploadLargeFile for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(UploadLargeFile, self).__init__('uploadlargefile.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class GetVendorList(REST):
    """ class: veracode.API.upload.GetVendorList

        params: dynamic, see veracode.SDK.upload.GetVendorList for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GetVendorList, self).__init__('getvendorlist.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class UpdateApp(REST):
    """ class: veracode.API.upload.UpdateApp

        params: dynamic, see veracode.SDK.upload.UpdateApp for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(UpdateApp, self).__init__('updateapp.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class GetFileList(REST):
    """ class: veracode.API.upload.GetFileList

        params: dynamic, see veracode.SDK.upload.GetFileList for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GetFileList, self).__init__('getfilelist.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class CreateBuild(REST):
    """ class: veracode.API.upload.CreateBuild

        params: dynamic, see veracode.SDK.upload.CreateBuild for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(CreateBuild, self).__init__('createbuild.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class GetPreScanResults(REST):
    """ class: veracode.API.upload.GetPreScanResults

        params: dynamic, see veracode.SDK.upload.GetPreScanResults for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GetPreScanResults, self).__init__('getprescanresults.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class CreateApp(REST):
    """ class: veracode.API.upload.CreateApp

        params: dynamic, see veracode.SDK.upload.CreateApp for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(CreateApp, self).__init__('createapp.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class GetBuildList(REST):
    """ class: veracode.API.upload.GetBuildList

        params: dynamic, see veracode.SDK.upload.GetBuildList for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(GetBuildList, self).__init__('getbuildlist.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class UploadFile(REST):
    """ class: veracode.API.upload.UploadFile

        params: dynamic, see veracode.SDK.upload.UploadFile for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(UploadFile, self).__init__('uploadfile.do', 5.0)

    @classmethod
    def post(self, **args):
        file = args['file']
        del args['file']
        return self().POST(args, file=file)


class BeginScan(REST):
    """ class: veracode.API.upload.BeginScan

        params: dynamic, see veracode.SDK.upload.BeginScan for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(BeginScan, self).__init__('beginscan.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')

class RemoveFile(REST):
    """ class: veracode.API.upload.RemoveFile

        params: dynamic, see veracode.SDK.upload.RemoveFile for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(RemoveFile, self).__init__('removefile.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


class DeleteApp(REST):
    """ class: veracode.API.upload.DeleteApp

        params: dynamic, see veracode.SDK.upload.DeleteApp for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super(DeleteApp, self).__init__('deleteapp.do', 5.0)

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')


