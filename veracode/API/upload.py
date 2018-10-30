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

class UpdateApp(REST):
    def __init__(self):
        super(UpdateApp, self).__init__('updateapp.do', 5.0)

    @classmethod
    def update(self, app_id, app_name,
            description=None,
            business_criticality=None,
            policy=None,
            business_unit=None,
            business_owner=None,
            business_owner_email=None,
            teams=None,
            origin=None,
            industry=None,
            app_type=None,
            deployment_method=None,
            archer_app_name=None,
            tags=None,
            custom_field_name=None,
            next_day_scheduling_enabled=None
            ):
        return self().GET({
           'app_id':app_id, 'app_name':app_name,
           'description':description,
           'business_criticality':business_criticality,
           'policy':policy,
           'business_unit':business_unit,
           'business_owner':business_owner,
           'business_owner_email':business_owner_email,
           'teams':teams,
           'origin':origin,
           'industry':industry,
           'app_type':app_type,
           'deployment_method':deployment_method,
           'archer_app_name':archer_app_name,
           'tags':tags,
           'custom_field_name':custom_field_name,
           'next_day_scheduling_enabled':next_day_scheduling_enabled
            })
