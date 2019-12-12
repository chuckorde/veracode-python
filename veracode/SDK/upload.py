from veracode.SDK.core import Base
import os

class GetAppList(Base):
    """ class: veracode.SDK.upload.GetAppList

        params:
            include_user_info: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self, include_user_info=None):

        super(GetAppList, self).__init__(
            module='upload',
            cls='GetAppList',
            fn='get',
            args={
                'include_user_info':include_user_info,
            })

class UpdateBuild(Base):
    """ class: veracode.SDK.upload.UpdateBuild

        params:
            build_id: required
            app_id: required
            version: optional
            sandbox_id: optional
            lifecycle_stage: optional
            launch_date: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                build_id,
                app_id,
                version=None,
                sandbox_id=None,
                lifecycle_stage=None,
                launch_date=None,
        ):

        super(UpdateBuild, self).__init__(
            module='upload',
            cls='UpdateBuild',
            fn='get',
            args={
                'build_id':build_id,
                'app_id':app_id,
                'version':version,
                'sandbox_id':sandbox_id,
                'lifecycle_stage':lifecycle_stage,
                'launch_date':launch_date,
            })

class DeleteBuild(Base):
    """ class: veracode.SDK.upload.DeleteBuild

        params:
            app_id: required
            sandbox_id: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                app_id,
                sandbox_id=None,
        ):

        super(DeleteBuild, self).__init__(
            module='upload',
            cls='DeleteBuild',
            fn='get',
            args={
                'app_id':app_id,
                'sandbox_id':sandbox_id,
            })

class GetBuildInfo(Base):
    """ class: veracode.SDK.upload.GetBuildInfo

        params:
            app_id: required
            sandbox_id: optional
            build_id: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                app_id,
                sandbox_id=None,
                build_id=None,
        ):

        super(GetBuildInfo, self).__init__(
            module='upload',
            cls='GetBuildInfo',
            fn='get',
            args={
                'app_id':app_id,
                'sandbox_id':sandbox_id,
                'build_id':build_id,
            })

class GetAppInfo(Base):
    """ class: veracode.SDK.upload.GetAppInfo

        params:
            app_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                app_id,
        ):

        super(GetAppInfo, self).__init__(
            module='upload',
            cls='GetAppInfo',
            fn='get',
            args={
                'app_id':app_id,
            })

class GetPolicyList(Base):
    """ class: veracode.SDK.upload.GetPolicyList

        params:


        returns: A python object that represents the returned API data.
    """
    def __init__(self,

        ):

        super(GetPolicyList, self).__init__(
            module='upload',
            cls='GetPolicyList',
            fn='get',
            args={

            })

class BeginPrescan(Base):
    """ class: veracode.SDK.upload.BeginPrescan

        params:
            app_id: required
            scan_all_nonfatal_top_level_modules: optional
            sandbox_id: optional
            auto_scan: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                app_id,
                scan_all_nonfatal_top_level_modules=None,
                sandbox_id=None,
                auto_scan=None,
        ):

        super(BeginPrescan, self).__init__(
            module='upload',
            cls='BeginPrescan',
            fn='get',
            args={
                'app_id':app_id,
                'scan_all_nonfatal_top_level_modules':scan_all_nonfatal_top_level_modules,
                'sandbox_id':sandbox_id,
                'auto_scan':auto_scan,
            })

class UploadLargeFile(Base):
    """ class: veracode.SDK.upload.UploadLargeFile

        params:
            file: required
            app_id: required
            save_as: optional
            sandbox_id: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                file,
                app_id,
                save_as=None,
                sandbox_id=None,
        ):

        super(UploadLargeFile, self).__init__(
            module='upload',
            cls='UploadLargeFile',
            fn='get',
            args={
                'file':file,
                'app_id':app_id,
                'save_as':save_as,
                'sandbox_id':sandbox_id,
            })

class GetVendorList(Base):
    """ class: veracode.SDK.upload.GetVendorList

        params:


        returns: A python object that represents the returned API data.
    """
    def __init__(self,

        ):

        super(GetVendorList, self).__init__(
            module='upload',
            cls='GetVendorList',
            fn='get',
            args={

            })

class UpdateApp(Base):
    """ class: veracode.SDK.upload.UpdateApp

        params:
            app_id: required
            app_name: required
            business_criticality: required
            web_application: optional
            teams: optional
            tags: optional
            policy: optional
            origin: optional
            next_day_scheduling_enabled: optional
            industry: optional
            description: optional
            deployment_method: optional
            custom_field_value: optional
            custom_field_name: optional
            business_unit: optional
            business_owner_email: optional
            business_owner: optional
            archer_app_name: optional
            app_type: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                app_id,
                app_name,
                business_criticality,
                web_application=None,
                teams=None,
                tags=None,
                policy=None,
                origin=None,
                next_day_scheduling_enabled=None,
                industry=None,
                description=None,
                deployment_method=None,
                custom_field_value=None,
                custom_field_name=None,
                business_unit=None,
                business_owner_email=None,
                business_owner=None,
                archer_app_name=None,
                app_type=None,
        ):

        super(UpdateApp, self).__init__(
            module='upload',
            cls='UpdateApp',
            fn='get',
            args={
                'app_id':app_id,
                'app_name':app_name,
                'business_criticality':business_criticality,
                'web_application':web_application,
                'teams':teams,
                'tags':tags,
                'policy':policy,
                'origin':origin,
                'next_day_scheduling_enabled':next_day_scheduling_enabled,
                'industry':industry,
                'description':description,
                'deployment_method':deployment_method,
                'custom_field_value':custom_field_value,
                'custom_field_name':custom_field_name,
                'business_unit':business_unit,
                'business_owner_email':business_owner_email,
                'business_owner':business_owner,
                'archer_app_name':archer_app_name,
                'app_type':app_type,
            })

class GetFileList(Base):
    """ class: veracode.SDK.upload.GetFileList

        params:
            app_id: required
            sandbox_id: optional
            build_id: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                app_id,
                sandbox_id=None,
                build_id=None,
        ):

        super(GetFileList, self).__init__(
            module='upload',
            cls='GetFileList',
            fn='get',
            args={
                'app_id':app_id,
                'sandbox_id':sandbox_id,
                'build_id':build_id,
            })

class CreateBuild(Base):
    """ class: veracode.SDK.upload.CreateBuild

        params:
            version: required
            app_id: required
            sandbox_id: optional
            platform: optional
            lifecycle_stage: optional
            launch_date: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                version,
                app_id,
                sandbox_id=None,
                platform=None,
                lifecycle_stage=None,
                launch_date=None,
        ):

        super(CreateBuild, self).__init__(
            module='upload',
            cls='CreateBuild',
            fn='get',
            args={
                'version':version,
                'app_id':app_id,
                'sandbox_id':sandbox_id,
                'platform':platform,
                'lifecycle_stage':lifecycle_stage,
                'launch_date':launch_date,
            })

class GetPreScanResults(Base):
    """ class: veracode.SDK.upload.GetPreScanResults

        params:
            app_id: required
            sandbox_id: optional
            build_id: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                app_id,
                sandbox_id=None,
                build_id=None,
        ):

        super(GetPreScanResults, self).__init__(
            module='upload',
            cls='GetPreScanResults',
            fn='get',
            args={
                'app_id':app_id,
                'sandbox_id':sandbox_id,
                'build_id':build_id,
            })

class CreateApp(Base):
    """ class: veracode.SDK.upload.CreateApp

        params:
            business_criticality: required
            app_name: required
            web_application: optional
            vendor_id: optional
            teams: optional
            tags: optional
            policy: optional
            origin: optional
            next_day_scheduling_enabled: optional
            industry: optional
            description: optional
            deployment_method: optional
            business_unit: optional
            business_owner_email: optional
            business_owner: optional
            archer_app_name: optional
            app_type: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                business_criticality,
                app_name,
                web_application=None,
                vendor_id=None,
                teams=None,
                tags=None,
                policy=None,
                origin=None,
                next_day_scheduling_enabled=None,
                industry=None,
                description=None,
                deployment_method=None,
                business_unit=None,
                business_owner_email=None,
                business_owner=None,
                archer_app_name=None,
                app_type=None,
        ):

        super(CreateApp, self).__init__(
            module='upload',
            cls='CreateApp',
            fn='get',
            args={
                'business_criticality':business_criticality,
                'app_name':app_name,
                'web_application':web_application,
                'vendor_id':vendor_id,
                'teams':teams,
                'tags':tags,
                'policy':policy,
                'origin':origin,
                'next_day_scheduling_enabled':next_day_scheduling_enabled,
                'industry':industry,
                'description':description,
                'deployment_method':deployment_method,
                'business_unit':business_unit,
                'business_owner_email':business_owner_email,
                'business_owner':business_owner,
                'archer_app_name':archer_app_name,
                'app_type':app_type,
            })

class GetBuildList(Base):
    """ class: veracode.SDK.upload.GetBuildList

        params:
            app_id: required
            sandbox_id: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                app_id,
                sandbox_id=None,
        ):

        super(GetBuildList, self).__init__(
            module='upload',
            cls='GetBuildList',
            fn='get',
            args={
                'app_id':app_id,
                'sandbox_id':sandbox_id,
            })

class UploadFile(Base):
    """ class: veracode.SDK.upload.UploadFile

        params:
            file: required
            app_id: required
            save_as: optional
            sandbox_id: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                file,
                app_id,
                save_as=None,
                sandbox_id=None,
        ):

        super(UploadFile, self).__init__(
            module='upload',
            cls='UploadFile',
            fn='post',
            args={
                'file':{
                    'file':(os.path.basename(file), open(file, 'rb').read())},
                'app_id':app_id,
                'save_as':save_as,
                'sandbox_id':sandbox_id,
            })

class BeginScan(Base):
    """ class: veracode.SDK.upload.BeginScan

        params:
            app_id: required
            scan_selected_modules: optional
            scan_previously_selected_modules: optional
            scan_all_top_level_modules: optional
            sandbox_id: optional
            modules: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                app_id,
                scan_selected_modules=None,
                scan_previously_selected_modules=None,
                scan_all_top_level_modules=None,
                sandbox_id=None,
                modules=None,
        ):

        super(BeginScan, self).__init__(
            module='upload',
            cls='BeginScan',
            fn='get',
            args={
                'app_id':app_id,
                'scan_selected_modules':scan_selected_modules,
                'scan_previously_selected_modules':scan_previously_selected_modules,
                'scan_all_top_level_modules':scan_all_top_level_modules,
                'sandbox_id':sandbox_id,
                'modules':modules,
            })

class RemoveFile(Base):
    """ class: veracode.SDK.upload.RemoveFile

        params:
            file_id: required
            app_id: required
            sandbox_id: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                file_id,
                app_id,
                sandbox_id=None,
        ):

        super(RemoveFile, self).__init__(
            module='upload',
            cls='RemoveFile',
            fn='get',
            args={
                'file_id':file_id,
                'app_id':app_id,
                'sandbox_id':sandbox_id,
            })

class DeleteApp(Base):
    """ class: veracode.SDK.upload.DeleteApp

        params:
            app_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                app_id,
        ):

        super(DeleteApp, self).__init__(
            module='upload',
            cls='DeleteApp',
            fn='get',
            args={
                'app_id':app_id,
            })

