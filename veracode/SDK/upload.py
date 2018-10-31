from veracode.SDK.core import Base


class CreateApp(Base):
    def __init__(self, app_name, business_criticality,
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
        super(CreateApp, self).__init__(
                module='admin',
                cls='CreateApp',
                fn='create',
                args={
                    'app_name':app_name,
                    'business_criticality':business_criticality,
                    'vendor_id':vendor_id,
                    'policy':policy,
                    'business_unit':business_unit,
                    'business_owner':business_owner,
                    'buisness_owner_email':buisness_owner_email,
                    'teams':','.join([t if teams else '' for t in teams]),
                    'origin':origin,
                    'industry':industry,
                    'app_type':app_type,
                    'deployment_method':deployment_method,
                    'web_application':web_application,
                    'archer_app_name':archer_app_name,
                    'tags':','.join([t if tags else '' for t in tags]),
                    'next_day_scheduling_enabled':next_day_scheduling_enabled
                })

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

class UpdateApp(Base):
    def __init__(self, 
            app_id, app_name,
            description=None,
            business_criticality=None,
            policy=None,
            business_unit=None,
            business_owner=None,
            business_owner_email=None,
            teams=[],
            origin=None,
            industry=None,
            app_type=None,
            deployment_method=None,
            archer_app_name=None,
            tags=None,
            custom_field_name=None,
            next_day_scheduling_enabled=None):
        super(UpdateApp, self).__init__(
                module='upload',
                cls='UpdateApp',
                fn='update',
                args={
                   'app_id':app_id, 'app_name':app_name,
                   'description':description,
                   'business_criticality':business_criticality,
                   'policy':policy,
                   'business_unit':business_unit,
                   'business_owner':business_owner,
                   'business_owner_email':business_owner_email,
                   'teams':','.join([t if teams else '' for t in teams]),
                   'origin':origin,
                   'industry':industry,
                   'app_type':app_type,
                   'deployment_method':deployment_method,
                   'archer_app_name':archer_app_name,
                   'tags':tags,
                   'custom_field_name':custom_field_name,
                   'next_day_scheduling_enabled':next_day_scheduling_enabled
                     })
