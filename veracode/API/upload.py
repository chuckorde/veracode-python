from veracode.API.core import REST


class BeginPreScan(REST):
    def __init__(self):
        super(BeginPreScan, self).__init__('beginprescan.do', 5.0)

    @classmethod
    def begin(self, app_id, 
            auto_scan=None, 
            sandbox_id=None, 
            scan_all_nonfatal_top_level_modules=None):
        return self().GET({
            'app_id':app_id, 
            'auto_scan':auto_scan,
            'sandbox_id':sandbox_id,
            'scan_all_nonfatal_top_level_modules': \
                    scan_all_nonfatal_top_level_modules
            })


class BeginScan(REST):
    def __init__(self):
        super(BeginScan, self).__init__('beginscan.do', 5.0)

    @classmethod
    def begin(self, app_id, 
            modules=None
            scan_all_top_level_modules=None,
            scan_selected_modules=None,
            scan_previously_selected_modules=None,
            sandbox_id=None):
        return self().GET({
            'app_id':app_id, 
            'modules':modules,
            'scan_all_top_level_modules':scan_all_top_level_modules,
            'scan_selected_modules':scan_selected_modules,
            'scan_previously_selected_modules':scan_previously_selected_modules,
            'sandbox_id':sandbox_id
            })

class CreateApp(REST):
    def __init__(self):
        super(CreateApp, self).__init__('createapp.do', 5.0)

    @classmethod
    def create(self, app_name, business_criticality,
            vendor_id=None,
            policy=None,
            business_unit=None,
            business_owner=None,
            buisness_owner_email=None,
            teams=None,
            origin=None,
            industry=None,
            app_type=None,
            deployment_method=None,
            web_application=None,
            archer_app_name=None,
            tags=None,
            next_day_scheduling_enabled=None
            ):
        return self().GET({
            'app_name':app_name,
            'business_criticality':business_criticality,
            'vendor_id':vendor_id,
            'policy':policy,
            'business_unit':business_unit,
            'business_owner':business_owner,
            'buisness_owner_email':buisness_owner_email,
            'teams':teams,
            'origin':origin,
            'industry':industry,
            'app_type':app_type,
            'deployment_method':deployment_method,
            'web_application':web_application,
            'archer_app_name':archer_app_name,
            'tags':tags,
            'next_day_scheduling_enabled':next_day_scheduling_enabled
            })


class CreateBuild(REST):
    def __init__(self):
        super(CreateBuild, self).__init__('createbuild.do', 5.0)

    @classmethod
    def create(self, app_id
            version,
            platform=None,
            lifecycle_stage=None,
            launch_date=None,
            sandbox_id=None,
            legacy_scan_engine=None):
        return self().GET({
            'app_id':app_id,
            'platform':platform,
            'lifecycle_stage':lifecycle_stage,
            'launch_date':launch_date,
            'sandbox_id':sandbox_id,
            'legacy_scan_engine':legacy_scan_engine
            })


class DeleteApp(REST):
    def __init__(self):
        super(DeleteApp, self).__init__('deleteapp.do', 5.0)

    @classmethod
    def delete(self, app_id, sandbox_id=None):
        return self().GET({'app_id':app_id, 'sandbox_id':sandbox_id})


class DeleteBuild(REST):
    def __init__(self):
        super(DeleteBuild, self).__init__('deletebuild.do', 5.0)

    @classmethod
    def delete(self, app_id, sandbox_id=None):
        return self().GET({'app_id':app_id, 'sandbox_id':sandbox_id})


class GetAppInfo(REST):
    def __init__(self):
        super(GetAppInfo, self).__init__('getappinfo.do', 5.0)

    @classmethod
    def get(self, app_id):
        return self().GET({'app_id':app_id})


class GetAppList(REST):
    def __init__(self):
        super(GetAppList, self).__init__('getapplist.do', 5.0)

    @classmethod
    def get(self, include_user_info=None):
        return self().GET({'include_user_info':include_user_info})


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


class RemoveFile(REST):
    def __init__(self):
        super(RemoveFile, self).__init__('removefile.do', 5.0)

    @classmethod
    def remove(self, app_id, file_id=None, sandbox_id=None):
        return self().GET({'app_id':app_id, 'file_id':file_id,
                           'sandbox_id':sandbox_id})


class UpdateApp(REST):
    def __init__(self):
        super(UpdateApp, self).__init__('updateapp.do', 5.0)

    @classmethod
    def update(self,
            app_id,
            app_name,
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
           'app_id':app_id,
           'app_name':app_name,
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


class UpdateBuild(REST):
    def __init__(self):
        super(UpdateBuild, self).__init__('updatebuild.do', 5.0)

    @classmethod
    def update(self,
            app_id,
            build_id,
            version,
            lifecycle_stage=None,
            launch_date=None,
            sandbox_id=None):
        return self().GET({
           'app_id':app_id,
           'build_id':build_id,
           'version':version,
           'lifecycle_stage':lifecycle_stage,
           'launch_date':launch_date,
           'sandbox_id':sandbox_id
            })


class UploadFile(REST):
    def __init__(self):
        super(UploadFile, self).__init__('uploadfile.do', 5.0)

    @classmethod
    def update(self,
            app_id,
            file,
            sandbox_id=None,
            save_as=None):
        return self().GET({
           'app_id':app_id,
           'file':file,
           'sandbox_id':sandbox_id
           'save_as':save_as
            })


